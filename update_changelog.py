"""
Huorong VirDB Changelog Updater

This script is designed to run daily in GitHub Actions to:
1. Download the latest Huorong installer
2. Extract the virus database
3. If new, compare with previous version and update README.md

Usage:
    python update_changelog.py
"""

import sys
import shutil
from pathlib import Path
from datetime import datetime, timezone
from typing import Optional, Set, List, Tuple

# Import from existing modules
from huorong_downloader import (
    get_latest_installer_url,
    download_installer,
    InstallerInfo
)
from extract_virdb import (
    extract_vfs_from_installer,
    find_7z,
    ExtractResult
)
from create_changelog import (
    CLI_TOOL,
    VIRDB_DIR,
    README_PATH,
    DATA_DIR,
    VirDBInfo,
    ChangelogEntry,
    get_version,
    get_info,
    get_virus_names,
    get_malware_hashes,
    get_whitelist_hashes,
    get_date_from_folder,
    get_virus_category,
    get_category_distribution,
    split_names_by_telemetry,
)


# Directory for downloaded installers
INSTALLERS_DIR = Path(__file__).parent / "installers"


def get_existing_virdb_folders() -> List[str]:
    """Get list of existing virdb folder names."""
    if not VIRDB_DIR.exists():
        return []
    return sorted([
        d.name for d in VIRDB_DIR.iterdir()
        if d.is_dir() and d.name.startswith("sysdiag-all-")
    ])


def installer_already_extracted(installer_name: str) -> bool:
    """Check if an installer has already been extracted."""
    virdb_path = VIRDB_DIR / installer_name
    return virdb_path.exists() and virdb_path.is_dir()


def download_and_extract_latest() -> Tuple[Optional[Path], bool]:
    """
    Download the latest installer and extract virdb.
    
    Returns:
        Tuple of (virdb_path, is_new) where is_new indicates if this is a new version.
    """
    print("=" * 60)
    print("Step 1: Fetching latest installer info")
    print("=" * 60)
    
    # Get latest installer info
    latest = get_latest_installer_url()
    if not latest:
        print("ERROR: Could not get latest installer info")
        return None, False
    
    print(f"  Latest: {latest.filename}")
    print(f"  Version: {latest.version}")
    print(f"  Date: {latest.date}")
    print(f"  URL: {latest.url}")
    print()
    
    # Check if already extracted
    installer_name = latest.filename.replace(".exe", "")
    if installer_already_extracted(installer_name):
        print(f"  Already extracted: {installer_name}")
        print("  Skipping download and extraction.")
        return VIRDB_DIR / installer_name, False
    
    print("=" * 60)
    print("Step 2: Downloading installer")
    print("=" * 60)
    
    # Download installer
    INSTALLERS_DIR.mkdir(parents=True, exist_ok=True)
    installer_path = download_installer(latest, INSTALLERS_DIR)
    
    if not installer_path:
        print("ERROR: Failed to download installer")
        return None, False
    
    print()
    print("=" * 60)
    print("Step 3: Extracting virus database")
    print("=" * 60)
    
    # Check for 7z
    seven_zip = find_7z()
    if not seven_zip:
        print("ERROR: 7-Zip not found!")
        print("Please install 7-Zip from https://www.7-zip.org/")
        return None, False
    
    print(f"  Using 7z: {seven_zip}")
    print()
    
    # Extract virdb
    result = extract_vfs_from_installer(installer_path, VIRDB_DIR)
    
    if not result.success:
        print(f"ERROR: Extraction failed: {result.error}")
        return None, False
    
    print()
    print(f"  Extracted {len(result.extracted_files)} files to {result.output_dir}")
    
    # Clean up installer to save space
    if installer_path.exists():
        installer_path.unlink()
        print(f"  Cleaned up: {installer_path.name}")
    
    return result.output_dir, True


def load_virdb_info(virdb_path: Path) -> Optional[VirDBInfo]:
    """Load all information about a virus database."""
    folder_name = virdb_path.name
    
    print(f"  Loading: {folder_name}")
    
    # Get version
    version_ts = get_version(virdb_path)
    if version_ts is None:
        print(f"    WARNING: Could not get version")
        return None
    
    version_dt = datetime.fromtimestamp(version_ts, tz=timezone.utc)
    
    # Get info
    info = get_info(virdb_path)
    if info is None:
        print(f"    WARNING: Could not get info")
        return None
    
    stats = info.get('statistics', {})
    
    # Get virus names
    print(f"    Extracting virus names...")
    virus_names = get_virus_names(virdb_path)
    print(f"    Found {len(virus_names):,} unique virus names")
    
    # Get malware hashes (blacklist)
    print(f"    Extracting malware hashes...")
    malware_hashes = get_malware_hashes(virdb_path)
    print(f"    Found {len(malware_hashes):,} malware hashes")
    
    # Get whitelist hashes
    print(f"    Extracting whitelist hashes...")
    whitelist_hashes = get_whitelist_hashes(virdb_path)
    print(f"    Found {len(whitelist_hashes):,} whitelist hashes")
    
    return VirDBInfo(
        path=virdb_path,
        folder_name=folder_name,
        version_timestamp=version_ts,
        version_datetime=version_dt,
        total_files=stats.get('files', 0),
        pset_records=stats.get('pset_records', 0),
        troj_hashes=stats.get('troj_hashes', 0),
        troj_names=stats.get('troj_names', 0),
        prop_profiles=stats.get('prop_hash_records', 0),
        prop_patterns=stats.get('prop_pattern_entries', 0),
        hwl_records=stats.get('hwl_records', 0),
        virus_names=virus_names,
        malware_hashes=malware_hashes,
        whitelist_hashes=whitelist_hashes
    )


def generate_single_changelog_entry(
    current: VirDBInfo,
    previous: Optional[VirDBInfo]
) -> ChangelogEntry:
    """Generate a changelog entry comparing current to previous version."""
    if previous is None:
        # First version - all are "new"
        all_new_names = sorted(current.virus_names)
        all_removed_names = []
        new_malware_hashes = sorted(current.malware_hashes)
        removed_malware_hashes = []
        new_whitelist_hashes = sorted(current.whitelist_hashes)
        removed_whitelist_hashes = []
    else:
        all_new_names = sorted(current.virus_names - previous.virus_names)
        all_removed_names = sorted(previous.virus_names - current.virus_names)
        new_malware_hashes = sorted(current.malware_hashes - previous.malware_hashes)
        removed_malware_hashes = sorted(previous.malware_hashes - current.malware_hashes)
        new_whitelist_hashes = sorted(current.whitelist_hashes - previous.whitelist_hashes)
        removed_whitelist_hashes = sorted(previous.whitelist_hashes - current.whitelist_hashes)
    
    # Split names into regular and telemetry
    new_names, new_names_telemetry = split_names_by_telemetry(all_new_names)
    removed_names, removed_names_telemetry = split_names_by_telemetry(all_removed_names)
    
    date_str = get_date_from_folder(current.folder_name) or current.version_datetime.strftime('%Y-%m-%d')
    
    return ChangelogEntry(
        date=date_str,
        version_timestamp=current.version_timestamp,
        version_datetime=current.version_datetime,
        folder_name=current.folder_name,
        new_names=new_names,
        removed_names=removed_names,
        new_names_telemetry=new_names_telemetry,
        removed_names_telemetry=removed_names_telemetry,
        new_malware_hashes=new_malware_hashes,
        removed_malware_hashes=removed_malware_hashes,
        new_whitelist_hashes=new_whitelist_hashes,
        removed_whitelist_hashes=removed_whitelist_hashes,
        total_names=len(current.virus_names),
        total_malware_hashes=len(current.malware_hashes),
        total_whitelist_hashes=len(current.whitelist_hashes),
        stats={
            'pset_records': current.pset_records,
            'troj_hashes': current.troj_hashes,
            'troj_names': current.troj_names,
            'prop_profiles': current.prop_profiles,
            'prop_patterns': current.prop_patterns,
            'hwl_records': current.hwl_records,
        }
    )


def compress_with_7z(file_path: Path) -> bool:
    """
    Compress a file using 7z and remove the original.
    
    Args:
        file_path: Path to the file to compress.
        
    Returns:
        True if successful, False otherwise.
    """
    import subprocess
    
    seven_zip = find_7z()
    if not seven_zip:
        print(f"    WARNING: 7z not found, skipping compression for {file_path.name}")
        return False
    
    archive_path = file_path.with_suffix(file_path.suffix + '.7z')
    
    try:
        result = subprocess.run(
            [str(seven_zip), 'a', '-mx=9', str(archive_path), str(file_path)],
            capture_output=True,
            text=True,
            timeout=120
        )
        
        if result.returncode == 0 and archive_path.exists():
            # Remove original file after successful compression
            file_path.unlink()
            return True
        else:
            print(f"    WARNING: Failed to compress {file_path.name}")
            return False
    except Exception as e:
        print(f"    WARNING: Compression error for {file_path.name}: {e}")
        return False


def write_single_data_file(entry: ChangelogEntry, virdb: VirDBInfo) -> None:
    """Write data files for a single changelog entry.
    
    Creates two types of files:
    - Incremental files (*.txt): Changes compared to previous version
    - Full snapshot files (*.full.txt.7z): Complete list of all items (compressed)
    """
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    
    version = entry.version_timestamp
    incremental_files = 0
    full_files = 0
    
    # Combine regular and telemetry names for data files
    all_new_names = entry.new_names + entry.new_names_telemetry
    all_removed_names = entry.removed_names + entry.removed_names_telemetry
    
    # Write detection names file if there are changes
    if all_new_names or all_removed_names:
        detection_file = DATA_DIR / f"{version}.pset.txt"
        detection_lines = []
        
        for name in sorted(all_new_names):
            detection_lines.append(f"[+] {name}")
        for name in sorted(all_removed_names):
            detection_lines.append(f"[-] {name}")
        
        with open(detection_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(detection_lines))
        incremental_files += 1
        print(f"    Written: {detection_file.name}")
    
    # Write full detection names snapshot (compressed)
    if virdb.virus_names:
        full_pset_file = DATA_DIR / f"{version}.pset.full.txt"
        with open(full_pset_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(sorted(virdb.virus_names)))
        if compress_with_7z(full_pset_file):
            full_files += 1
            print(f"    Written: {full_pset_file.name}.7z")
    
    # Write malware hashes (troj) file if there are changes
    if entry.new_malware_hashes or entry.removed_malware_hashes:
        troj_file = DATA_DIR / f"{version}.troj.txt"
        troj_lines = []
        
        for h in sorted(entry.new_malware_hashes):
            troj_lines.append(f"[+] {h}")
        for h in sorted(entry.removed_malware_hashes):
            troj_lines.append(f"[-] {h}")
        
        with open(troj_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(troj_lines))
        incremental_files += 1
        print(f"    Written: {troj_file.name}")
    
    # Write full malware hashes snapshot (compressed)
    if virdb.malware_hashes:
        full_troj_file = DATA_DIR / f"{version}.troj.full.txt"
        with open(full_troj_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(sorted(virdb.malware_hashes)))
        if compress_with_7z(full_troj_file):
            full_files += 1
            print(f"    Written: {full_troj_file.name}.7z")
    
    # Write whitelist hashes (hwl) file if there are changes
    if entry.new_whitelist_hashes or entry.removed_whitelist_hashes:
        hwl_file = DATA_DIR / f"{version}.hwl.txt"
        hwl_lines = []
        
        for h in sorted(entry.new_whitelist_hashes):
            hwl_lines.append(f"[+] {h}")
        for h in sorted(entry.removed_whitelist_hashes):
            hwl_lines.append(f"[-] {h}")
        
        with open(hwl_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(hwl_lines))
        incremental_files += 1
        print(f"    Written: {hwl_file.name}")
    
    # Write full whitelist hashes snapshot (compressed)
    if virdb.whitelist_hashes:
        full_hwl_file = DATA_DIR / f"{version}.hwl.full.txt"
        with open(full_hwl_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(sorted(virdb.whitelist_hashes)))
        if compress_with_7z(full_hwl_file):
            full_files += 1
            print(f"    Written: {full_hwl_file.name}.7z")
    
    print(f"  Written {incremental_files} incremental + {full_files} compressed full snapshot files")


def update_changelog(new_virdb_path: Path) -> bool:
    """
    Update the changelog with a new virus database version.
    
    This function efficiently updates by:
    1. Loading only the previous latest virdb (for comparison)
    2. Loading the new virdb
    3. Generating a single changelog entry
    4. Updating README.md incrementally
    
    Args:
        new_virdb_path: Path to the newly extracted virdb folder.
        
    Returns:
        True if successful, False otherwise.
    """
    print()
    print("=" * 60)
    print("Step 4: Updating changelog")
    print("=" * 60)
    
    # Check CLI tool
    if not CLI_TOOL.exists():
        print(f"ERROR: CLI tool not found: {CLI_TOOL}")
        return False
    
    # Find all virdb folders and sort them
    virdb_folders = sorted([
        d for d in VIRDB_DIR.iterdir()
        if d.is_dir() and d.name.startswith("sysdiag-all-")
    ])
    
    if not virdb_folders:
        print("ERROR: No virdb folders found")
        return False
    
    total_versions = len(virdb_folders)
    print(f"  Total virdb versions: {total_versions}")
    
    # Find the previous latest (second to last after sorting)
    # The new_virdb_path should be the latest
    previous_virdb_path = None
    if total_versions >= 2:
        # Find the previous version (not the new one)
        for folder in reversed(virdb_folders):
            if folder != new_virdb_path:
                previous_virdb_path = folder
                break
    
    print()
    print("Loading version information (efficient mode)...")
    print("-" * 40)
    
    # Load the new virdb
    print(f"Loading NEW virdb:")
    new_virdb = load_virdb_info(new_virdb_path)
    if new_virdb is None:
        print("ERROR: Could not load new virdb")
        return False
    
    # Load the previous virdb (if exists)
    previous_virdb = None
    if previous_virdb_path:
        print()
        print(f"Loading PREVIOUS virdb:")
        previous_virdb = load_virdb_info(previous_virdb_path)
        if previous_virdb is None:
            print("WARNING: Could not load previous virdb, treating as first version")
    
    print()
    print("Generating changelog entry...")
    print("-" * 40)
    
    # Generate the new changelog entry
    new_entry = generate_single_changelog_entry(new_virdb, previous_virdb)
    
    print(f"  New regular detections: {len(new_entry.new_names):,}")
    print(f"  Removed regular detections: {len(new_entry.removed_names):,}")
    print(f"  New telemetry detections: {len(new_entry.new_names_telemetry):,}")
    print(f"  Removed telemetry detections: {len(new_entry.removed_names_telemetry):,}")
    print(f"  New malware hashes: {len(new_entry.new_malware_hashes):,}")
    print(f"  New whitelist hashes: {len(new_entry.new_whitelist_hashes):,}")
    print()
    
    # Write data files for the new entry only
    print("Writing data files for new entry...")
    write_single_data_file(new_entry, new_virdb)
    print()
    
    # Update README.md incrementally
    print("Updating README.md...")
    success = update_readme_incrementally(new_entry, new_virdb.virus_names, total_versions)
    
    if success:
        print(f"  Updated: {README_PATH}")
    
    return success


def format_single_changelog_entry(entry: ChangelogEntry, is_oldest: bool = False) -> str:
    """Format a single changelog entry for insertion into README."""
    lines = []
    
    lines.append(f"### {entry.date}")
    lines.append("")
    lines.append(f"**版本**: `{entry.version_timestamp}` ({entry.version_datetime.strftime('%Y-%m-%d %H:%M:%S UTC')})")
    lines.append("")
    
    # Detection names - show with foldable details (separate regular and telemetry)
    has_regular = entry.new_names or entry.removed_names
    has_telemetry = entry.new_names_telemetry or entry.removed_names_telemetry
    
    if has_regular or has_telemetry:
        lines.append(f"#### 检测项变更 ([pset.txt](data/{entry.version_timestamp}.pset.txt))")
        lines.append("")
        
        if is_oldest:
            # Oldest entry: just show counts without foldable details
            if has_regular:
                summary_parts = []
                if entry.new_names:
                    summary_parts.append(f"新增: {len(entry.new_names):,}")
                if entry.removed_names:
                    summary_parts.append(f"移除: {len(entry.removed_names):,}")
                lines.append(f"**正式定义**: {' | '.join(summary_parts)}")
                lines.append("")
            if has_telemetry:
                summary_parts = []
                if entry.new_names_telemetry:
                    summary_parts.append(f"新增: {len(entry.new_names_telemetry):,}")
                if entry.removed_names_telemetry:
                    summary_parts.append(f"移除: {len(entry.removed_names_telemetry):,}")
                lines.append(f"**遥测定义**: {' | '.join(summary_parts)}")
                lines.append("")
        else:
            # Other entries: show foldable details
            # Regular definitions section
            if has_regular:
                lines.append("<details>")
                lines.append("<summary>")
                summary_parts = []
                if entry.new_names:
                    summary_parts.append(f"新增正式定义: {len(entry.new_names):,}")
                if entry.removed_names:
                    summary_parts.append(f"移除正式定义: {len(entry.removed_names):,}")
                lines.append(" | ".join(summary_parts))
                lines.append("</summary>")
                lines.append("")
                lines.append("```")
                for name in entry.new_names:
                    lines.append(f"[+] {name}")
                for name in entry.removed_names:
                    lines.append(f"[-] {name}")
                lines.append("```")
                lines.append("")
                lines.append("</details>")
                lines.append("")
            
            # Telemetry definitions section
            if has_telemetry:
                lines.append("<details>")
                lines.append("<summary>")
                summary_parts = []
                if entry.new_names_telemetry:
                    summary_parts.append(f"新增遥测定义: {len(entry.new_names_telemetry):,}")
                if entry.removed_names_telemetry:
                    summary_parts.append(f"移除遥测定义: {len(entry.removed_names_telemetry):,}")
                lines.append(" | ".join(summary_parts))
                lines.append("</summary>")
                lines.append("")
                lines.append("```")
                for name in entry.new_names_telemetry:
                    lines.append(f"[+] {name}")
                for name in entry.removed_names_telemetry:
                    lines.append(f"[-] {name}")
                lines.append("```")
                lines.append("")
                lines.append("</details>")
                lines.append("")
    
    # Malware hashes (blacklist)
    if entry.new_malware_hashes or entry.removed_malware_hashes:
        lines.append(f"#### 黑名单哈希变更 ([troj.txt](data/{entry.version_timestamp}.troj.txt))")
        lines.append("")
        troj_parts = []
        if entry.new_malware_hashes:
            troj_parts.append(f"新增: {len(entry.new_malware_hashes):,}")
        if entry.removed_malware_hashes:
            troj_parts.append(f"移除: {len(entry.removed_malware_hashes):,}")
        lines.append(" | ".join(troj_parts))
        lines.append("")
    
    # Whitelist hashes
    if entry.new_whitelist_hashes or entry.removed_whitelist_hashes:
        lines.append(f"#### 白名单哈希变更 ([hwl.txt](data/{entry.version_timestamp}.hwl.txt))")
        lines.append("")
        hwl_parts = []
        if entry.new_whitelist_hashes:
            hwl_parts.append(f"新增: {len(entry.new_whitelist_hashes):,}")
        if entry.removed_whitelist_hashes:
            hwl_parts.append(f"移除: {len(entry.removed_whitelist_hashes):,}")
        lines.append(" | ".join(hwl_parts))
        lines.append("")
    
    # Stats summary as table
    lines.append("**统计**:")
    lines.append("")
    lines.append("| 指标 | 数值 |")
    lines.append("|------|-----:|")
    lines.append(f"| 检测项总数 | {entry.total_names:,} |")
    lines.append(f"| 黑名单哈希总数 | {entry.total_malware_hashes:,} |")
    lines.append(f"| 白名单哈希总数 | {entry.total_whitelist_hashes:,} |")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    return "\n".join(lines)


def update_readme_incrementally(
    new_entry: ChangelogEntry,
    latest_virus_names: Set[str],
    total_versions: int
) -> bool:
    """
    Update README.md incrementally by:
    1. Updating the overview section with new stats
    2. Inserting the new changelog entry at the top of the changelog
    
    Args:
        new_entry: The new changelog entry to add.
        latest_virus_names: Set of virus names from the latest virdb.
        total_versions: Total number of tracked versions.
        
    Returns:
        True if successful, False otherwise.
    """
    import re
    
    if not README_PATH.exists():
        print("  ERROR: README.md does not exist, cannot update incrementally")
        return False
    
    with open(README_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update overview section
    # Update 最新版本
    content = re.sub(
        r'- \*\*最新版本\*\*: `\d+` \([^)]+\)',
        f'- **最新版本**: `{new_entry.version_timestamp}` ({new_entry.version_datetime.strftime("%Y-%m-%d %H:%M:%S UTC")})',
        content
    )
    
    # Update 检测项总数
    content = re.sub(
        r'- \*\*检测项总数\*\*: [\d,]+',
        f'- **检测项总数**: {new_entry.total_names:,}',
        content
    )
    
    # Update 黑名单哈希总数
    content = re.sub(
        r'- \*\*黑名单哈希总数\*\*: [\d,]+',
        f'- **黑名单哈希总数**: {new_entry.total_malware_hashes:,}',
        content
    )
    
    # Update 白名单哈希总数
    content = re.sub(
        r'- \*\*白名单哈希总数\*\*: [\d,]+',
        f'- **白名单哈希总数**: {new_entry.total_whitelist_hashes:,}',
        content
    )
    
    # Update 已跟踪版本数
    content = re.sub(
        r'- \*\*已跟踪版本数\*\*: \d+',
        f'- **已跟踪版本数**: {total_versions}',
        content
    )
    
    # Update the pie chart section
    distribution = get_category_distribution(latest_virus_names)
    pie_chart_lines = []
    pie_chart_lines.append("```mermaid")
    pie_chart_lines.append("pie showData")
    pie_chart_lines.append("    title Top 10")
    for category, count in distribution.items():
        pie_chart_lines.append(f'    "{category}" : {count}')
    pie_chart_lines.append("```")
    new_pie_chart = "\n".join(pie_chart_lines)
    
    # Replace the existing pie chart
    content = re.sub(
        r'```mermaid\npie showData\n    title Top 10\n(?:    "[^"]+" : \d+\n)+```',
        new_pie_chart,
        content
    )
    
    # Insert new changelog entry after "## 更新日志\n\n"
    new_entry_text = format_single_changelog_entry(new_entry, is_oldest=False)
    
    # Find the position to insert (after "## 更新日志\n\n")
    changelog_marker = "## 更新日志\n\n"
    insert_pos = content.find(changelog_marker)
    
    if insert_pos == -1:
        print("  ERROR: Could not find '## 更新日志' marker in README.md")
        return False
    
    insert_pos += len(changelog_marker)
    
    # Insert the new entry
    content = content[:insert_pos] + new_entry_text + content[insert_pos:]
    
    # Write back
    with open(README_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True
    
    return True


def main() -> int:
    """Main entry point."""
    print("=" * 60)
    print("Huorong VirDB Changelog Updater")
    print(f"Run at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    print()
    
    # Download and extract latest
    new_virdb_path, is_new = download_and_extract_latest()
    
    if new_virdb_path is None:
        print()
        print("=" * 60)
        print("Update FAILED!")
        print("=" * 60)
        return 1
    
    if not is_new:
        print()
        print("=" * 60)
        print("No new version available. Changelog is up to date.")
        print("=" * 60)
        return 0
    
    # Update changelog
    success = update_changelog(new_virdb_path)
    
    print()
    print("=" * 60)
    if success:
        print("Update completed successfully!")
        print(f"New virdb: {new_virdb_path.name}")
    else:
        print("Update FAILED!")
    print("=" * 60)
    
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())

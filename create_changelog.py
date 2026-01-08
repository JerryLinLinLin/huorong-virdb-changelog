"""
Huorong VirDB Changelog Generator

This script generates a changelog by comparing virus names across different
versions of the Huorong virus database. It extracts virus names using the
huorong_virdb_cli tool and creates a professional README.md changelog.

This is a one-time initialization script to create the initial changelog.
"""

import subprocess
import json
import tempfile
import os
from pathlib import Path
from datetime import datetime, timezone
from dataclasses import dataclass
from typing import Optional, Set, List

from extract_virdb import find_7z


# CLI tool paths
CLI_TOOL = Path(__file__).parent / "bin" / "huorong_virdb_cli-windows-x64.exe"
BEHAV_CLI_TOOL = Path(__file__).parent / "bin" / "huorong_behavdb_cli.exe"
VIRDB_DIR = Path(__file__).parent / "virdb"
README_PATH = Path(__file__).parent / "README.md"
DATA_DIR = Path(__file__).parent / "data"


@dataclass
class VirDBInfo:
    """Information about a virus database version."""
    path: Path
    folder_name: str
    version_timestamp: int
    version_datetime: datetime
    total_files: int
    pset_records: int
    troj_hashes: int
    troj_names: int
    prop_profiles: int
    prop_patterns: int
    hwl_records: int
    virus_names: Set[str]
    malware_hashes: Set[str]
    whitelist_hashes: Set[str]
    behavior_names: Set[str]


@dataclass
class ChangelogEntry:
    """A changelog entry representing changes between versions."""
    date: str
    version_timestamp: int
    version_datetime: datetime
    folder_name: str
    new_names: List[str]
    removed_names: List[str]
    new_names_telemetry: List[str]  # Names containing !submit
    removed_names_telemetry: List[str]  # Names containing !submit
    new_malware_hashes: List[str]
    removed_malware_hashes: List[str]
    new_whitelist_hashes: List[str]
    removed_whitelist_hashes: List[str]
    new_behavior_names: List[str]
    removed_behavior_names: List[str]
    total_names: int
    total_malware_hashes: int
    total_whitelist_hashes: int
    total_behavior_names: int
    stats: dict


def is_telemetry_name(name: str) -> bool:
    """Check if a detection name is a telemetry detection (contains !submit)."""
    return '!submit' in name.lower()


def split_names_by_telemetry(names: List[str]) -> tuple[List[str], List[str]]:
    """
    Split detection names into regular and telemetry categories.
    
    Args:
        names: List of detection names.
        
    Returns:
        Tuple of (regular_names, telemetry_names).
    """
    regular = []
    telemetry = []
    for name in names:
        if is_telemetry_name(name):
            telemetry.append(name)
        else:
            regular.append(name)
    return regular, telemetry


def compress_with_7z(file_path: Path) -> bool:
    """
    Compress a file using 7z and remove the original.
    
    Args:
        file_path: Path to the file to compress.
        
    Returns:
        True if successful, False otherwise.
    """
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


def run_cli(args: List[str]) -> tuple[bool, str]:
    """
    Run the huorong_virdb_cli tool.
    
    Args:
        args: Command line arguments.
        
    Returns:
        Tuple of (success, output/error).
    """
    if not CLI_TOOL.exists():
        return False, f"CLI tool not found: {CLI_TOOL}"
    
    try:
        cmd = [str(CLI_TOOL)] + args
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=300
        )
        return True, result.stdout
    except subprocess.TimeoutExpired:
        return False, "Command timed out"
    except Exception as e:
        return False, str(e)


def get_version(virdb_path: Path) -> Optional[int]:
    """Get the version timestamp from a virdb."""
    success, output = run_cli(["version", str(virdb_path), "--simple"])
    if success:
        try:
            return int(output.strip())
        except ValueError:
            return None
    return None


def get_info(virdb_path: Path) -> Optional[dict]:
    """Get detailed info from a virdb as JSON."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_path = Path(f.name)
    
    try:
        success, _ = run_cli(["info", str(virdb_path), "-o", str(temp_path)])
        if success and temp_path.exists():
            with open(temp_path, 'r', encoding='utf-8') as f:
                return json.load(f)
    finally:
        if temp_path.exists():
            temp_path.unlink()
    return None


def get_virus_names(virdb_path: Path) -> Set[str]:
    """Extract all virus names from a virdb."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        temp_path = Path(f.name)
    
    try:
        success, _ = run_cli(["names", str(virdb_path), "-o", str(temp_path)])
        if success and temp_path.exists():
            with open(temp_path, 'r', encoding='utf-8') as f:
                names = set(line.strip() for line in f if line.strip())
                return names
    finally:
        if temp_path.exists():
            temp_path.unlink()
    return set()


def get_malware_hashes(virdb_path: Path) -> Set[str]:
    """Extract all malware (blacklist) hashes from a virdb."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        temp_path = Path(f.name)
    
    try:
        success, _ = run_cli(["malware-hashes", str(virdb_path), "-o", str(temp_path)])
        if success and temp_path.exists():
            with open(temp_path, 'r', encoding='utf-8') as f:
                hashes = set(line.strip() for line in f if line.strip())
                return hashes
    finally:
        if temp_path.exists():
            temp_path.unlink()
    return set()


def get_whitelist_hashes(virdb_path: Path) -> Set[str]:
    """Extract all whitelist hashes from a virdb."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        temp_path = Path(f.name)
    
    try:
        success, _ = run_cli(["whitelist", str(virdb_path), "-o", str(temp_path)])
        if success and temp_path.exists():
            with open(temp_path, 'r', encoding='utf-8') as f:
                hashes = set(line.strip() for line in f if line.strip())
                return hashes
    finally:
        if temp_path.exists():
            temp_path.unlink()
    return set()


def run_behav_cli(args: List[str]) -> tuple[bool, str]:
    """
    Run the huorong_behavdb_cli tool.
    
    Args:
        args: Command line arguments.
        
    Returns:
        Tuple of (success, output/error).
    """
    if not BEHAV_CLI_TOOL.exists():
        return False, f"Behavior CLI tool not found: {BEHAV_CLI_TOOL}"
    
    try:
        cmd = [str(BEHAV_CLI_TOOL)] + args
        # Set env vars to disable rich fancy output (avoids Unicode errors on Windows)
        env = os.environ.copy()
        env['NO_COLOR'] = '1'
        env['TERM'] = 'dumb'
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=300,
            env=env
        )
        return True, result.stdout
    except subprocess.TimeoutExpired:
        return False, "Command timed out"
    except Exception as e:
        return False, str(e)


def get_behavior_names(virdb_path: Path) -> Set[str]:
    """Extract all behavior signature names from a virdb (behav.db.vfs)."""
    behav_db_path = virdb_path / "behav.db.vfs"
    if not behav_db_path.exists():
        print(f"    WARNING: behav.db.vfs not found in {virdb_path.name}")
        return set()
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        temp_path = Path(f.name)
    
    try:
        success, _ = run_behav_cli(["names", str(behav_db_path), "-o", str(temp_path)])
        if success and temp_path.exists():
            with open(temp_path, 'r', encoding='utf-8') as f:
                names = set(line.strip() for line in f if line.strip())
                return names
    finally:
        if temp_path.exists():
            temp_path.unlink()
    return set()


def get_date_from_folder(folder_name: str) -> Optional[str]:
    """Extract date from folder name like 'sysdiag-all-x64-6.0.8.5-2025.12.25.1'."""
    import re
    match = re.search(r'-(\d{4})\.(\d{2})\.(\d{2})\.\d+$', folder_name)
    if match:
        return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
    return None


def get_virus_category(virus_name: str) -> str:
    """
    Extract category from virus name.
    
    Examples:
        Trojan/Injector.atw -> Trojan
        HEUR:Backdoor/CobaltStrike.bc -> Backdoor
        HVM:TrojanDownloader/Agent.cd -> TrojanDownloader
        ADV:Adware/Agent.a -> Adware
    """
    # Remove prefix like HEUR:, HVM:, ADV:, etc.
    if ':' in virus_name:
        virus_name = virus_name.split(':', 1)[1]
    
    # Get category (part before /)
    if '/' in virus_name:
        return virus_name.split('/')[0]
    
    return virus_name


def get_category_distribution(virus_names: Set[str], top_n: int = 10) -> dict:
    """Get distribution of virus names by category, limited to top N with Others."""
    from collections import Counter
    categories = [get_virus_category(name) for name in virus_names]
    counter = Counter(categories)
    
    # Get top N categories
    top_categories = counter.most_common(top_n)
    
    # Calculate "Other" count
    top_count = sum(count for _, count in top_categories)
    other_count = len(categories) - top_count
    
    result = dict(top_categories)
    if other_count > 0:
        result["Other"] = other_count
    
    return result


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
    
    # Get behavior names
    print(f"    Extracting behavior names...")
    behavior_names = get_behavior_names(virdb_path)
    print(f"    Found {len(behavior_names):,} behavior names")
    
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
        whitelist_hashes=whitelist_hashes,
        behavior_names=behavior_names
    )


def generate_changelog(versions: List[VirDBInfo]) -> List[ChangelogEntry]:
    """Generate changelog entries by comparing consecutive versions."""
    entries = []
    
    for i, current in enumerate(versions):
        if i == 0:
            # First version - all are "new"
            all_new_names = sorted(current.virus_names)
            all_removed_names = []
            new_malware_hashes = sorted(current.malware_hashes)
            removed_malware_hashes = []
            new_whitelist_hashes = sorted(current.whitelist_hashes)
            removed_whitelist_hashes = []
            new_behavior_names = sorted(current.behavior_names)
            removed_behavior_names = []
        else:
            previous = versions[i - 1]
            all_new_names = sorted(current.virus_names - previous.virus_names)
            all_removed_names = sorted(previous.virus_names - current.virus_names)
            new_malware_hashes = sorted(current.malware_hashes - previous.malware_hashes)
            removed_malware_hashes = sorted(previous.malware_hashes - current.malware_hashes)
            new_whitelist_hashes = sorted(current.whitelist_hashes - previous.whitelist_hashes)
            removed_whitelist_hashes = sorted(previous.whitelist_hashes - current.whitelist_hashes)
            new_behavior_names = sorted(current.behavior_names - previous.behavior_names)
            removed_behavior_names = sorted(previous.behavior_names - current.behavior_names)
        
        # Split names into regular and telemetry
        new_names, new_names_telemetry = split_names_by_telemetry(all_new_names)
        removed_names, removed_names_telemetry = split_names_by_telemetry(all_removed_names)
        
        date_str = get_date_from_folder(current.folder_name) or current.version_datetime.strftime('%Y-%m-%d')
        
        entry = ChangelogEntry(
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
            new_behavior_names=new_behavior_names,
            removed_behavior_names=removed_behavior_names,
            total_names=len(current.virus_names),
            total_malware_hashes=len(current.malware_hashes),
            total_whitelist_hashes=len(current.whitelist_hashes),
            total_behavior_names=len(current.behavior_names),
            stats={
                'pset_records': current.pset_records,
                'troj_hashes': current.troj_hashes,
                'troj_names': current.troj_names,
                'prop_profiles': current.prop_profiles,
                'prop_patterns': current.prop_patterns,
                'hwl_records': current.hwl_records,
            }
        )
        entries.append(entry)
    
    return entries


def write_data_files(entries: List[ChangelogEntry], versions: List[VirDBInfo]) -> None:
    """Write detection and hash changes to separate files in the data directory.
    
    Creates two types of files for each version:
    - Incremental files (*.txt): Changes compared to previous version
    - Full snapshot files (*.full.txt.7z): Complete list of all items (compressed)
    """
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    
    incremental_files = 0
    full_files = 0
    
    # Create a mapping from version_timestamp to VirDBInfo for full snapshots
    version_map = {v.version_timestamp: v for v in versions}
    
    for entry in entries:
        version = entry.version_timestamp
        virdb = version_map.get(version)
        
        # Write detection names file if there are changes (include both regular and telemetry)
        all_new_names = entry.new_names + entry.new_names_telemetry
        all_removed_names = entry.removed_names + entry.removed_names_telemetry
        has_detection_changes = all_new_names or all_removed_names
        if has_detection_changes:
            detection_file = DATA_DIR / f"{version}.pset.txt"
            detection_lines = []
            
            for name in sorted(all_new_names):
                detection_lines.append(f"[+] {name}")
            for name in sorted(all_removed_names):
                detection_lines.append(f"[-] {name}")
            
            with open(detection_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(detection_lines))
            incremental_files += 1
        
        # Write full detection names snapshot (compressed)
        if virdb and virdb.virus_names:
            full_pset_file = DATA_DIR / f"{version}.pset.full.txt"
            with open(full_pset_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(sorted(virdb.virus_names)))
            if compress_with_7z(full_pset_file):
                full_files += 1
        
        # Write behavior names (behav) file if there are changes
        has_behav_changes = entry.new_behavior_names or entry.removed_behavior_names
        if has_behav_changes:
            behav_file = DATA_DIR / f"{version}.behav.txt"
            behav_lines = []
            
            for name in sorted(entry.new_behavior_names):
                behav_lines.append(f"[+] {name}")
            for name in sorted(entry.removed_behavior_names):
                behav_lines.append(f"[-] {name}")
            
            with open(behav_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(behav_lines))
            incremental_files += 1
        
        # Write full behavior names snapshot (compressed)
        if virdb and virdb.behavior_names:
            full_behav_file = DATA_DIR / f"{version}.behav.full.txt"
            with open(full_behav_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(sorted(virdb.behavior_names)))
            if compress_with_7z(full_behav_file):
                full_files += 1
        
        # Write malware hashes (troj) file if there are changes
        has_troj_changes = entry.new_malware_hashes or entry.removed_malware_hashes
        if has_troj_changes:
            troj_file = DATA_DIR / f"{version}.troj.txt"
            troj_lines = []
            
            for h in sorted(entry.new_malware_hashes):
                troj_lines.append(f"[+] {h}")
            for h in sorted(entry.removed_malware_hashes):
                troj_lines.append(f"[-] {h}")
            
            with open(troj_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(troj_lines))
            incremental_files += 1
        
        # Write full malware hashes snapshot (compressed)
        if virdb and virdb.malware_hashes:
            full_troj_file = DATA_DIR / f"{version}.troj.full.txt"
            with open(full_troj_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(sorted(virdb.malware_hashes)))
            if compress_with_7z(full_troj_file):
                full_files += 1
        
        # Write whitelist hashes (hwl) file if there are changes
        has_hwl_changes = entry.new_whitelist_hashes or entry.removed_whitelist_hashes
        if has_hwl_changes:
            hwl_file = DATA_DIR / f"{version}.hwl.txt"
            hwl_lines = []
            
            for h in sorted(entry.new_whitelist_hashes):
                hwl_lines.append(f"[+] {h}")
            for h in sorted(entry.removed_whitelist_hashes):
                hwl_lines.append(f"[-] {h}")
            
            with open(hwl_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(hwl_lines))
            incremental_files += 1
        
        # Write full whitelist hashes snapshot (compressed)
        if virdb and virdb.whitelist_hashes:
            full_hwl_file = DATA_DIR / f"{version}.hwl.full.txt"
            with open(full_hwl_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(sorted(virdb.whitelist_hashes)))
            if compress_with_7z(full_hwl_file):
                full_files += 1
    
    print(f"  Written {incremental_files} incremental + {full_files} compressed full snapshot files to {DATA_DIR}")


def format_readme(entries: List[ChangelogEntry], latest_virus_names: Set[str] = None) -> str:
    """Generate the README.md content."""
    lines = []
    
    # Header
    lines.append("# 火绒病毒库更新日志")
    lines.append("")
    lines.append("本仓库跟踪[火绒安全软件](https://www.huorong.cn/)病毒库的变更，通过读取`pset.db,troj.db,hwl.db,behav.db`自动生成与上一版本相比新增的特征项/报毒名, 黑名单哈希和白名单哈希。")
    lines.append("")
    lines.append("> **免责声明**：本项目非火绒官方出品，仅供学习和技术交流使用。作者不对使用本项目造成的任何后果负责。")
    lines.append("")
    lines.append("## 概览")
    lines.append("")
    
    if entries:
        latest = entries[-1]
        lines.append(f"- **最新版本**: `{latest.version_timestamp}` ({latest.version_datetime.strftime('%Y-%m-%d %H:%M:%S UTC')})")
        lines.append(f"- **特征项总数**: {latest.total_names:,}")
        lines.append(f"- **行为特征项总数**: {latest.total_behavior_names:,}")
        lines.append(f"- **黑名单哈希总数**: {latest.total_malware_hashes:,}")
        lines.append(f"- **白名单哈希总数**: {latest.total_whitelist_hashes:,}")
        lines.append(f"- **已跟踪版本数**: {len(entries)}")
        lines.append("")
        
        # Add pie chart for virus category distribution
        if latest_virus_names:
            distribution = get_category_distribution(latest_virus_names)
            lines.append("## 特征项分类分布")
            lines.append("")
            lines.append("```mermaid")
            lines.append("pie showData")
            lines.append("    title Top 10")
            for category, count in distribution.items():
                lines.append(f'    "{category}" : {count}')
            lines.append("```")
            lines.append("")
        lines.append("")
    
    lines.append("---")
    lines.append("")
    lines.append("## 更新日志")
    lines.append("")
    
    # Changelog entries (newest first)
    reversed_entries = list(reversed(entries))
    oldest_version = entries[0].version_timestamp if entries else None
    
    for entry in reversed_entries:
        # Start foldable entry
        lines.append("<details>")
        lines.append(f"<summary><b>{entry.version_timestamp}</b> - {entry.version_datetime.strftime('%Y-%m-%d %H:%M:%S UTC')}</summary>")
        lines.append("")
        
        # Detection names - show with foldable details (oldest entry shows only counts, no details)
        is_oldest = entry.version_timestamp == oldest_version
        has_regular_changes = entry.new_names or entry.removed_names
        has_telemetry_changes = entry.new_names_telemetry or entry.removed_names_telemetry
        
        if has_regular_changes or has_telemetry_changes:
            lines.append(f"#### 特征项变更 ([pset.txt](data/{entry.version_timestamp}.pset.txt))")
            lines.append("")

            # Regular definitions (正式定义)
            if has_regular_changes:
                if is_oldest:
                    # Oldest entry: just show counts without foldable details
                    summary_parts = []
                    if entry.new_names:
                        summary_parts.append(f"新增正式定义: {len(entry.new_names):,}")
                    if entry.removed_names:
                        summary_parts.append(f"移除正式定义: {len(entry.removed_names):,}")
                    lines.append(" | ".join(summary_parts))
                    lines.append("")
                else:
                    # Other entries: show foldable details
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
            
            # Telemetry definitions (遥测定义)
            if has_telemetry_changes:
                if is_oldest:
                    # Oldest entry: just show counts without foldable details
                    summary_parts = []
                    if entry.new_names_telemetry:
                        summary_parts.append(f"新增遥测定义: {len(entry.new_names_telemetry):,}")
                    if entry.removed_names_telemetry:
                        summary_parts.append(f"移除遥测定义: {len(entry.removed_names_telemetry):,}")
                    lines.append(" | ".join(summary_parts))
                    lines.append("")
                else:
                    # Other entries: show foldable details
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
        
        # Behavior signatures - show with foldable details
        has_behavior_changes = entry.new_behavior_names or entry.removed_behavior_names
        if has_behavior_changes:
            lines.append(f"#### 行为特征项变更 ([behav.txt](data/{entry.version_timestamp}.behav.txt))")
            lines.append("")
            
            if is_oldest:
                # Oldest entry: just show counts without foldable details
                summary_parts = []
                if entry.new_behavior_names:
                    summary_parts.append(f"新增: {len(entry.new_behavior_names):,}")
                if entry.removed_behavior_names:
                    summary_parts.append(f"移除: {len(entry.removed_behavior_names):,}")
                lines.append(" | ".join(summary_parts))
                lines.append("")
            else:
                # Other entries: show foldable details
                lines.append("<details>")
                lines.append("<summary>")
                summary_parts = []
                if entry.new_behavior_names:
                    summary_parts.append(f"新增: {len(entry.new_behavior_names):,}")
                if entry.removed_behavior_names:
                    summary_parts.append(f"移除: {len(entry.removed_behavior_names):,}")
                lines.append(" | ".join(summary_parts))
                lines.append("</summary>")
                lines.append("")
                lines.append("```")
                for name in entry.new_behavior_names:
                    lines.append(f"[+] {name}")
                for name in entry.removed_behavior_names:
                    lines.append(f"[-] {name}")
                lines.append("```")
                lines.append("")
                lines.append("</details>")
                lines.append("")
        
        # Malware hashes (blacklist) - only show counts with link to file
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
        
        # Whitelist hashes - only show counts with link to file
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
        
        lines.append("</details>")
        lines.append("")
    
    # Footer
    lines.append("## 许可协议")
    lines.append("")
    lines.append("本更新日志仅供参考。火绒病毒库为火绒安全软件所有。")
    lines.append("")
    
    return "\n".join(lines)


def main():
    """Main entry point."""
    print("=" * 60)
    print("Huorong VirDB Changelog Generator")
    print("=" * 60)
    print()
    
    # Check CLI tool
    if not CLI_TOOL.exists():
        print(f"ERROR: CLI tool not found: {CLI_TOOL}")
        return 1
    
    print(f"CLI Tool: {CLI_TOOL}")
    print(f"VirDB Directory: {VIRDB_DIR}")
    print()
    
    # Find all virdb folders
    if not VIRDB_DIR.exists():
        print(f"ERROR: VirDB directory not found: {VIRDB_DIR}")
        return 1
    
    virdb_folders = sorted([
        d for d in VIRDB_DIR.iterdir()
        if d.is_dir() and d.name.startswith("sysdiag-all-")
    ])
    
    if not virdb_folders:
        print("ERROR: No virdb folders found")
        return 1
    
    print(f"Found {len(virdb_folders)} virdb versions")
    print()
    
    # Load all version info
    print("Loading version information...")
    print("-" * 40)
    
    versions = []
    for folder in virdb_folders:
        info = load_virdb_info(folder)
        if info:
            versions.append(info)
    
    print()
    print(f"Successfully loaded {len(versions)} versions")
    print()
    
    if not versions:
        print("ERROR: No versions could be loaded")
        return 1
    
    # Sort by version timestamp
    versions.sort(key=lambda v: v.version_timestamp)
    
    # Generate changelog
    print("Generating changelog...")
    print("-" * 40)
    
    entries = generate_changelog(versions)
    
    # Summary
    total_new = sum(len(e.new_names) for e in entries[1:])  # Exclude first version
    total_removed = sum(len(e.removed_names) for e in entries)
    
    print(f"  Changelog entries: {len(entries)}")
    print(f"  Total new detections (across updates): {total_new:,}")
    print(f"  Total removed detections: {total_removed:,}")
    print()
    
    # Write data files
    print("Writing data files...")
    write_data_files(entries, versions)
    print()
    
    # Write README
    print("Writing README.md...")
    latest_virus_names = versions[-1].virus_names if versions else set()
    readme_content = format_readme(entries, latest_virus_names)
    
    with open(README_PATH, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"  Written to: {README_PATH}")
    print()
    print("=" * 60)
    print("Changelog generation complete!")
    print("=" * 60)
    
    return 0


if __name__ == "__main__":
    exit(main())

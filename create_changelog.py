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
from pathlib import Path
from datetime import datetime, timezone
from dataclasses import dataclass
from typing import Optional, Set, List


# CLI tool path
CLI_TOOL = Path(__file__).parent / "bin" / "huorong_virdb_cli-windows-x64.exe"
VIRDB_DIR = Path(__file__).parent / "virdb"
README_PATH = Path(__file__).parent / "README.md"


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


@dataclass
class ChangelogEntry:
    """A changelog entry representing changes between versions."""
    date: str
    version_timestamp: int
    version_datetime: datetime
    folder_name: str
    new_names: List[str]
    removed_names: List[str]
    total_names: int
    stats: dict


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


def get_date_from_folder(folder_name: str) -> Optional[str]:
    """Extract date from folder name like 'sysdiag-all-x64-6.0.8.5-2025.12.25.1'."""
    import re
    match = re.search(r'-(\d{4})\.(\d{2})\.(\d{2})\.\d+$', folder_name)
    if match:
        return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
    return None


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
        virus_names=virus_names
    )


def generate_changelog(versions: List[VirDBInfo]) -> List[ChangelogEntry]:
    """Generate changelog entries by comparing consecutive versions."""
    entries = []
    
    for i, current in enumerate(versions):
        if i == 0:
            # First version - all names are "new"
            new_names = sorted(current.virus_names)
            removed_names = []
        else:
            previous = versions[i - 1]
            new_names = sorted(current.virus_names - previous.virus_names)
            removed_names = sorted(previous.virus_names - current.virus_names)
        
        date_str = get_date_from_folder(current.folder_name) or current.version_datetime.strftime('%Y-%m-%d')
        
        entry = ChangelogEntry(
            date=date_str,
            version_timestamp=current.version_timestamp,
            version_datetime=current.version_datetime,
            folder_name=current.folder_name,
            new_names=new_names,
            removed_names=removed_names,
            total_names=len(current.virus_names),
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


def format_readme(entries: List[ChangelogEntry]) -> str:
    """Generate the README.md content."""
    lines = []
    
    # Header
    lines.append("# 🛡️ Huorong Virus Database Changelog")
    lines.append("")
    lines.append("This repository tracks changes to the [Huorong Internet Security](https://www.huorong.cn/) virus database.")
    lines.append("Each update shows newly added detection entries compared to the previous version.")
    lines.append("")
    lines.append("## 📊 Overview")
    lines.append("")
    
    if entries:
        latest = entries[-1]
        lines.append(f"- **Latest Version**: `{latest.version_timestamp}` ({latest.version_datetime.strftime('%Y-%m-%d %H:%M:%S UTC')})")
        lines.append(f"- **Total Detection Entries**: {latest.total_names:,}")
        lines.append(f"- **Versions Tracked**: {len(entries)}")
        lines.append("")
        
        # Statistics table
        lines.append("### Database Statistics (Latest)")
        lines.append("")
        lines.append("| Category | Count |")
        lines.append("|----------|------:|")
        lines.append(f"| PSET Records | {latest.stats['pset_records']:,} |")
        lines.append(f"| TROJ Hashes | {latest.stats['troj_hashes']:,} |")
        lines.append(f"| TROJ Names | {latest.stats['troj_names']:,} |")
        lines.append(f"| PROP Behavior Profiles | {latest.stats['prop_profiles']:,} |")
        lines.append(f"| PROP Pattern Entries | {latest.stats['prop_patterns']:,} |")
        lines.append(f"| HWL Records | {latest.stats['hwl_records']:,} |")
        lines.append("")
    
    lines.append("---")
    lines.append("")
    lines.append("## 📝 Changelog")
    lines.append("")
    
    # Changelog entries (newest first)
    for entry in reversed(entries):
        lines.append(f"### 📅 {entry.date}")
        lines.append("")
        lines.append(f"**VirDB Version**: `{entry.version_timestamp}` ({entry.version_datetime.strftime('%Y-%m-%d %H:%M:%S UTC')})")
        lines.append("")
        
        # New detections
        if entry.new_names:
            lines.append(f"#### ✅ New Detection Entries ({len(entry.new_names):,})")
            lines.append("")
            lines.append("<details>")
            lines.append("<summary>Click to expand</summary>")
            lines.append("")
            lines.append("```")
            for name in entry.new_names:
                lines.append(name)
            lines.append("```")
            lines.append("")
            lines.append("</details>")
            lines.append("")
        else:
            lines.append("#### ✅ New Detection Entries (0)")
            lines.append("")
            lines.append("_No new entries in this version._")
            lines.append("")
        
        # Removed detections (if any)
        if entry.removed_names:
            lines.append(f"#### ❌ Removed Detection Entries ({len(entry.removed_names):,})")
            lines.append("")
            lines.append("<details>")
            lines.append("<summary>Click to expand</summary>")
            lines.append("")
            lines.append("```")
            for name in entry.removed_names:
                lines.append(name)
            lines.append("```")
            lines.append("")
            lines.append("</details>")
            lines.append("")
        
        # Stats summary
        lines.append("**Statistics**:")
        lines.append(f"- Total Detection Entries: {entry.total_names:,}")
        lines.append(f"- PSET Records: {entry.stats['pset_records']:,}")
        lines.append(f"- TROJ Hashes: {entry.stats['troj_hashes']:,}")
        lines.append(f"- HWL Records: {entry.stats['hwl_records']:,}")
        lines.append("")
        lines.append("---")
        lines.append("")
    
    # Footer
    lines.append("## 🔧 Tools Used")
    lines.append("")
    lines.append("- [huorong_virdb_cli](https://github.com/AuroraTea/huorong-virdb-cli) - Huorong VirDB extraction tool")
    lines.append("")
    lines.append("## 📄 License")
    lines.append("")
    lines.append("This changelog is provided for informational purposes. Huorong virus database is property of Huorong.")
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
    
    # Write README
    print("Writing README.md...")
    readme_content = format_readme(entries)
    
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

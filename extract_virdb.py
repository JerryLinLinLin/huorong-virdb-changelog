"""
Huorong Virus Database Extractor

This module provides functions to extract virus database files (.vfs)
from Huorong Internet Security installers.
"""

import subprocess
import shutil
import tempfile
from pathlib import Path
from typing import Optional, List
from dataclasses import dataclass


@dataclass
class ExtractResult:
    """Result of extraction operation."""
    installer_name: str
    output_dir: Path
    extracted_files: List[str]
    success: bool
    error: Optional[str] = None


# Files to extract from the installer
TARGET_VFS_FILES = [
    "pset.db.vfs",
    "prop.db.vfs", 
    "troj.db.vfs",
    "hwl.db.vfs",
    "crithash.db.vfs",
]

# Path inside the installer to the vdb zip
INNER_ZIP_PATH = "$_14_/dist-tree-main-vdb.zip"
# Path inside the zip to the bases folder
BASES_PATH = "dist-tree-main/bases"


def find_7z() -> Optional[Path]:
    """
    Find system-installed 7z executable on Windows.
    
    Checks common installation paths including GitHub Actions Windows environment
    where 7-Zip is pre-installed at C:\\Program Files\\7-Zip\\7z.exe.
    
    Returns:
        Path to 7z.exe, or None if not found.
    """
    # Common locations for 7z on Windows (including GitHub Actions)
    possible_paths = [
        Path(r"C:\Program Files\7-Zip\7z.exe"),
        Path(r"C:\Program Files (x86)\7-Zip\7z.exe"),
    ]
    
    # Check if 7z is in PATH
    if shutil.which("7z"):
        return Path(shutil.which("7z"))
    
    if shutil.which("7z.exe"):
        return Path(shutil.which("7z.exe"))
    
    # Check common installation paths
    for path in possible_paths:
        if path.exists():
            return path
    
    return None


def run_7z(args: List[str], cwd: Optional[Path] = None) -> tuple[bool, str]:
    """
    Run 7z command with given arguments.
    
    Args:
        args: List of arguments to pass to 7z.
        cwd: Working directory for the command.
        
    Returns:
        Tuple of (success, output/error message).
    """
    seven_zip = find_7z()
    if not seven_zip:
        return False, "7-Zip not found. Please install 7-Zip from https://www.7-zip.org/"
    
    try:
        cmd = [str(seven_zip)] + args
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=cwd,
            timeout=120
        )
        
        if result.returncode == 0:
            return True, result.stdout
        else:
            return False, result.stderr or result.stdout
            
    except subprocess.TimeoutExpired:
        return False, "Command timed out"
    except Exception as e:
        return False, str(e)


def extract_vfs_from_installer(
    installer_path: Path,
    output_base_dir: Path = Path("./virdb"),
    target_files: Optional[List[str]] = None
) -> ExtractResult:
    """
    Extract virus database files from a Huorong installer.
    
    The installer structure is:
    - installer.exe (NSIS archive)
      - $_14_/dist-tree-main-vdb.zip
        - dist-tree-main/bases/
          - *.vfs files
    
    Args:
        installer_path: Path to the installer exe file.
        output_base_dir: Base directory for output (default: ./virdb).
        target_files: List of .vfs files to extract (default: predefined list).
        
    Returns:
        ExtractResult with extraction status and details.
    """
    installer_path = Path(installer_path)
    output_base_dir = Path(output_base_dir)
    target_files = target_files or TARGET_VFS_FILES
    
    # Get installer name without extension for output folder
    installer_name = installer_path.stem
    output_dir = output_base_dir / installer_name
    
    result = ExtractResult(
        installer_name=installer_name,
        output_dir=output_dir,
        extracted_files=[],
        success=False
    )
    
    if not installer_path.exists():
        result.error = f"Installer not found: {installer_path}"
        return result
    
    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Use a temporary directory for intermediate extraction
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        
        print(f"Extracting from: {installer_path.name}")
        
        # Step 1: Extract the inner zip from the installer
        # 7z e installer.exe $_14_/dist-tree-main-vdb.zip -oTEMP
        inner_zip_name = "dist-tree-main-vdb.zip"
        success, msg = run_7z([
            "e",  # extract without directory structure
            str(installer_path),
            INNER_ZIP_PATH,
            f"-o{temp_path}",
            "-y"  # assume yes
        ])
        
        if not success:
            result.error = f"Failed to extract inner zip: {msg}"
            return result
        
        inner_zip_path = temp_path / inner_zip_name
        if not inner_zip_path.exists():
            result.error = f"Inner zip not found after extraction: {inner_zip_name}"
            return result
        
        print(f"  Extracted: {inner_zip_name}")
        
        # Step 2: Extract target .vfs files from the inner zip
        # 7z e dist-tree-main-vdb.zip dist-tree-main/bases/*.vfs -oTEMP
        for vfs_file in target_files:
            vfs_path_in_zip = f"{BASES_PATH}/{vfs_file}"
            
            success, msg = run_7z([
                "e",
                str(inner_zip_path),
                vfs_path_in_zip,
                f"-o{temp_path}",
                "-y"
            ])
            
            if success:
                extracted_vfs = temp_path / vfs_file
                if extracted_vfs.exists():
                    # Copy to output, keeping .db.vfs extension
                    output_file = output_dir / vfs_file
                    shutil.copy2(extracted_vfs, output_file)
                    result.extracted_files.append(vfs_file)
                    print(f"  Extracted: {vfs_file}")
    
    if result.extracted_files:
        result.success = True
        print(f"  Output: {output_dir}")
    else:
        result.error = "No files were extracted"
    
    return result


def extract_all_installers(
    installers_dir: Path = Path("./installers"),
    output_base_dir: Path = Path("./virdb"),
    target_files: Optional[List[str]] = None
) -> List[ExtractResult]:
    """
    Extract virus database files from all installers in a directory.
    
    Args:
        installers_dir: Directory containing installer exe files.
        output_base_dir: Base directory for output.
        target_files: List of .vfs files to extract.
        
    Returns:
        List of ExtractResult for each installer.
    """
    installers_dir = Path(installers_dir)
    results = []
    
    if not installers_dir.exists():
        print(f"Installers directory not found: {installers_dir}")
        return results
    
    # Find all exe files
    exe_files = sorted(installers_dir.glob("sysdiag-all-*.exe"))
    
    if not exe_files:
        print(f"No installer files found in: {installers_dir}")
        return results
    
    print(f"Found {len(exe_files)} installers")
    print("=" * 60)
    
    for exe_path in exe_files:
        result = extract_vfs_from_installer(
            exe_path,
            output_base_dir,
            target_files
        )
        results.append(result)
        print()
    
    # Summary
    successful = sum(1 for r in results if r.success)
    print("=" * 60)
    print(f"Extraction complete: {successful}/{len(results)} successful")
    
    return results


def get_installer_date(installer_name: str) -> Optional[str]:
    """
    Extract the date from an installer name.
    
    Args:
        installer_name: Name like 'sysdiag-all-x64-6.0.8.5-2026.01.03.1'
        
    Returns:
        Date string like '2026.01.03' or None.
    """
    import re
    match = re.search(r"-(\d{4}\.\d{2}\.\d{2})\.\d+$", installer_name)
    if match:
        return match.group(1)
    return None


def list_extracted_databases(virdb_dir: Path = Path("./virdb")) -> dict:
    """
    List all extracted virus database directories.
    
    Args:
        virdb_dir: Base directory containing extracted databases.
        
    Returns:
        Dictionary mapping installer names to list of extracted files.
    """
    virdb_dir = Path(virdb_dir)
    result = {}
    
    if not virdb_dir.exists():
        return result
    
    for subdir in sorted(virdb_dir.iterdir()):
        if subdir.is_dir():
            files = [f.name for f in subdir.iterdir() if f.is_file()]
            result[subdir.name] = files
    
    return result


# Test/demo code
if __name__ == "__main__":
    print("=" * 60)
    print("Testing Virus Database Extractor")
    print("=" * 60)
    
    # Check for 7z
    seven_zip = find_7z()
    if seven_zip:
        print(f"Found 7z: {seven_zip}")
    else:
        print("ERROR: 7-Zip not found!")
        print("Please install 7-Zip from https://www.7-zip.org/")
        print("On GitHub Actions Windows, 7-Zip should be pre-installed.")
        exit(1)
    
    print()
    
    # Check for installers
    installers_dir = Path("./installers")
    if installers_dir.exists():
        exe_files = list(installers_dir.glob("sysdiag-all-*.exe"))
        print(f"Found {len(exe_files)} installers in {installers_dir}")
        
        if exe_files:
            print()
            # Extract from all installers
            results = extract_all_installers()
            
            print()
            print("Extracted databases:")
            for name, files in list_extracted_databases().items():
                print(f"  {name}/")
                for f in files:
                    print(f"    - {f}")
    else:
        print(f"No installers directory found at {installers_dir}")
        print("Run huorong_downloader.py first to download installers.")

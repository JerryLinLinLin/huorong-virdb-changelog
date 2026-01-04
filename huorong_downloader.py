"""
Huorong Internet Security Installer Downloader

This module provides functions to download the latest and previous
Huorong Internet Security installers.
"""

import re
import requests
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional, Tuple, List
from dataclasses import dataclass


@dataclass
class InstallerInfo:
    """Information about a Huorong installer."""
    url: str
    version: str
    date: str
    build: str
    arch: str
    filename: str


# Base URL pattern for Huorong installers
BASE_DOWNLOAD_URL = "https://down-tencent.huorong.cn"
REDIRECT_URL = "https://www.huorong.cn/product/downloadHr60.php?pro=hr60"

# URL pattern: sysdiag-all-{arch}-{major}.{minor}.{patch}.{revision}-{year}.{month}.{day}.{build}.exe
URL_PATTERN = re.compile(
    r"sysdiag-all-(x86|x64)-(\d+\.\d+\.\d+\.\d+)-(\d{4})\.(\d{2})\.(\d{2})\.(\d+)\.exe"
)


def get_latest_installer_url(arch: str = "x64") -> Optional[InstallerInfo]:
    """
    Get the latest installer URL by following the redirect.
    
    Args:
        arch: Architecture, either 'x64' or 'x86'. Default is 'x64'.
        
    Returns:
        InstallerInfo object with installer details, or None if failed.
    """
    try:
        # Follow redirect to get actual URL
        response = requests.head(REDIRECT_URL, allow_redirects=True, timeout=10)
        actual_url = response.url
        
        # Parse the URL to extract info
        info = parse_installer_url(actual_url)
        
        if info and info.arch != arch:
            # Construct URL for requested architecture
            new_url = actual_url.replace(f"-{info.arch}-", f"-{arch}-")
            info = parse_installer_url(new_url)
            
        return info
        
    except requests.RequestException as e:
        print(f"Error fetching latest installer URL: {e}")
        return None


def parse_installer_url(url: str) -> Optional[InstallerInfo]:
    """
    Parse an installer URL to extract version and date information.
    
    Args:
        url: The installer URL to parse.
        
    Returns:
        InstallerInfo object or None if parsing failed.
    """
    match = URL_PATTERN.search(url)
    if not match:
        return None
    
    arch, version, year, month, day, build = match.groups()
    date_str = f"{year}.{month}.{day}"
    filename = f"sysdiag-all-{arch}-{version}-{date_str}.{build}.exe"
    
    return InstallerInfo(
        url=url,
        version=version,
        date=date_str,
        build=build,
        arch=arch,
        filename=filename
    )


def construct_installer_url(
    version: str,
    date: datetime,
    build: str = "1",
    arch: str = "x64"
) -> str:
    """
    Construct an installer URL from components.
    
    Args:
        version: Version string like "6.0.8.5"
        date: Date object
        build: Build number, default "1"
        arch: Architecture, default "x64"
        
    Returns:
        Constructed URL string.
    """
    date_str = date.strftime("%Y.%m.%d")
    filename = f"sysdiag-all-{arch}-{version}-{date_str}.{build}.exe"
    return f"{BASE_DOWNLOAD_URL}/{filename}"


def check_url_exists(url: str, timeout: int = 5) -> bool:
    """
    Check if a URL exists (returns 200 status).
    
    Args:
        url: URL to check.
        timeout: Request timeout in seconds.
        
    Returns:
        True if URL exists, False otherwise.
    """
    try:
        response = requests.head(url, timeout=timeout, allow_redirects=True)
        return response.status_code == 200
    except requests.RequestException:
        return False


def guess_previous_version(version: str) -> str:
    """
    Guess the previous version by decrementing the revision number.
    
    Args:
        version: Current version like "6.0.8.5"
        
    Returns:
        Previous version like "6.0.8.4"
    """
    parts = version.split(".")
    if len(parts) == 4:
        revision = int(parts[3])
        if revision > 0:
            parts[3] = str(revision - 1)
    return ".".join(parts)


def find_previous_installers(
    count: int = 10,
    arch: str = "x64",
    start_date: Optional[datetime] = None,
    start_version: Optional[str] = None
) -> List[InstallerInfo]:
    """
    Find previous installer URLs by guessing dates and versions.
    
    This function tries to find previous installers by:
    1. Starting from the latest known installer
    2. Going back day by day
    3. Trying different version numbers if the current one doesn't exist
    
    Args:
        count: Number of previous installers to find (default 10).
        arch: Architecture, default "x64".
        start_date: Starting date (default: today).
        start_version: Starting version (default: from latest installer).
        
    Returns:
        List of InstallerInfo objects for found installers.
    """
    found_installers = []
    found_dates = set()  # Track dates we've already found
    
    # Get latest installer info if not provided
    if start_version is None or start_date is None:
        latest = get_latest_installer_url(arch)
        if latest:
            if start_version is None:
                start_version = latest.version
            if start_date is None:
                # Parse date from latest
                year, month, day = latest.date.split(".")
                start_date = datetime(int(year), int(month), int(day))
        else:
            # Fallback defaults
            start_date = start_date or datetime.now()
            start_version = start_version or "6.0.8.5"
    
    current_date = start_date
    current_version = start_version
    versions_to_try = [current_version]
    
    # Pre-generate some previous versions to try
    temp_ver = current_version
    for _ in range(5):
        temp_ver = guess_previous_version(temp_ver)
        if temp_ver not in versions_to_try:
            versions_to_try.append(temp_ver)
    
    max_days_back = 60  # Don't go more than 60 days back
    days_checked = 0
    
    print(f"Starting search from version {current_version}, date {current_date.strftime('%Y.%m.%d')}")
    print(f"Will try versions: {versions_to_try}")
    
    while len(found_installers) < count and days_checked < max_days_back:
        date_str = current_date.strftime("%Y.%m.%d")
        
        # Skip if we already found an installer for this date
        if date_str not in found_dates:
            # Try all versions for this date
            for version in versions_to_try:
                url = construct_installer_url(version, current_date, "1", arch)
                
                if check_url_exists(url):
                    info = parse_installer_url(url)
                    if info:
                        found_installers.append(info)
                        found_dates.add(date_str)
                        print(f"Found: {info.filename}")
                        
                        # Update version priority - put found version first
                        if version != versions_to_try[0]:
                            versions_to_try.remove(version)
                            versions_to_try.insert(0, version)
                        break
        
        # Go back one day
        current_date -= timedelta(days=1)
        days_checked += 1
    
    return found_installers


def download_installer(
    installer: InstallerInfo,
    output_dir: Optional[Path] = None,
    show_progress: bool = True
) -> Optional[Path]:
    """
    Download an installer to the specified directory.
    
    Args:
        installer: InstallerInfo object with URL and filename.
        output_dir: Output directory (default: current directory).
        show_progress: Show download progress (default: True).
        
    Returns:
        Path to downloaded file, or None if failed.
    """
    output_dir = output_dir or Path.cwd()
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_path = output_dir / installer.filename
    
    try:
        print(f"Downloading: {installer.filename}")
        response = requests.get(installer.url, stream=True, timeout=30)
        response.raise_for_status()
        
        total_size = int(response.headers.get("content-length", 0))
        downloaded = 0
        
        with open(output_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                downloaded += len(chunk)
                
                if show_progress and total_size > 0:
                    percent = (downloaded / total_size) * 100
                    print(f"\rProgress: {percent:.1f}% ({downloaded}/{total_size} bytes)", end="")
        
        if show_progress:
            print()  # New line after progress
            
        print(f"Downloaded: {output_path}")
        return output_path
        
    except requests.RequestException as e:
        print(f"Error downloading {installer.filename}: {e}")
        return None


def download_latest_installer(
    arch: str = "x64",
    output_dir: Optional[Path] = None
) -> Optional[Path]:
    """
    Download the latest installer.
    
    Args:
        arch: Architecture, default "x64".
        output_dir: Output directory (default: current directory).
        
    Returns:
        Path to downloaded file, or None if failed.
    """
    installer = get_latest_installer_url(arch)
    if installer:
        return download_installer(installer, output_dir)
    return None


def download_previous_installers(
    count: int = 10,
    arch: str = "x64",
    output_dir: Optional[Path] = None
) -> List[Path]:
    """
    Download previous installers.
    
    Args:
        count: Number of installers to download (default 10).
        arch: Architecture, default "x64".
        output_dir: Output directory (default: current directory).
        
    Returns:
        List of paths to downloaded files.
    """
    installers = find_previous_installers(count, arch)
    downloaded = []
    
    for installer in installers:
        path = download_installer(installer, output_dir)
        if path:
            downloaded.append(path)
    
    return downloaded


# For testing
if __name__ == "__main__":
    print("=" * 60)
    print("Testing Huorong Downloader")
    print("=" * 60)
    
    # Test 1: Get latest installer URL
    print("\n1. Getting latest installer URL...")
    latest = get_latest_installer_url()
    if latest:
        print(f"   URL: {latest.url}")
        print(f"   Version: {latest.version}")
        print(f"   Date: {latest.date}")
        print(f"   Arch: {latest.arch}")
        print(f"   Filename: {latest.filename}")
    else:
        print("   Failed to get latest installer URL")
    
    # Test 2: Check if URL exists
    print("\n2. Checking if URL exists...")
    if latest:
        exists = check_url_exists(latest.url)
        print(f"   URL exists: {exists}")
    
    # Test 3: Find previous installers
    print("\n3. Finding previous installers...")
    previous = find_previous_installers(count=10)
    print(f"\n   Found {len(previous)} installers:")
    for i, inst in enumerate(previous, 1):
        print(f"   {i}. {inst.filename} - {inst.url}")

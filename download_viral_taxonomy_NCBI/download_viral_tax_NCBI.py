#!/usr/bin/env python3

import os
import argparse
import subprocess

"""
Patricia Agudelo-Romero, PhD.
"""

def download_and_extract_taxonomy(url, output_dir):
    """
    Download the NCBI taxonomy dump and extract its contents.

    Args:
        url (str): URL to download the taxonomy dump.
        output_dir (str): Directory to save the downloaded and extracted files.
    """
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Step 1: Download the file
    print(f"Downloading taxonomy dump from: {url}")
    download_command = [
        "aria2c",
        "--file-allocation=none",
        "-c",  # Continue downloads
        "-x", "10",  # Use 10 connections
        "-s", "10",  # Use 10 split parts
        "-d", output_dir,
        url
    ]
    try:
        subprocess.run(download_command, check=True)
        print("Download completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during download: {e}")
        return

    # Step 2: Extract the downloaded file
    downloaded_file = os.path.join(output_dir, os.path.basename(url))
    print(f"Extracting file: {downloaded_file}")
    extract_command = [
        "tar", "-xvzf", downloaded_file, "-C", output_dir
    ]
    try:
        subprocess.run(extract_command, check=True)
        print(f"Extraction completed. Files are saved in: {output_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Error during extraction: {e}")
        return

    # Step 3: Remove the tar.gz file
    print(f"Removing downloaded file: {downloaded_file}")
    try:
        os.remove(downloaded_file)
        print("Downloaded .tar.gz file removed successfully.")
    except OSError as e:
        print(f"Error removing file {downloaded_file}: {e}")


if __name__ == "__main__":
    # Command-line argument parsing
    parser = argparse.ArgumentParser(
        description="Download and extract NCBI taxonomy dump."
    )
    parser.add_argument(
        "--url",
        default="ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/taxdump.tar.gz",
        help="URL to download the taxonomy dump. Default: NCBI taxonomy dump URL."
    )
    parser.add_argument(
        "--output-dir",
        default="TAX_nt",
        help="Output directory for downloaded and extracted files. Default: 'TAX_nt'."
    )

    # Parse arguments
    args = parser.parse_args()

    # Execute the download and extraction process
    download_and_extract_taxonomy(url=args.url, output_dir=args.output_dir)

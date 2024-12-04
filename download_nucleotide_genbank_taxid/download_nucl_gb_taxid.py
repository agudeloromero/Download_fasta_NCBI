#!/usr/bin/env python3

import os
import argparse
import subprocess


__author__ = "Patricia Agudelo-Romero, PhD."


def download_file(url, output_dir):
    """Download the file from the given URL to the specified output directory."""
    command = [
        "aria2c",
        "--file-allocation=none",
        "-c",
        "-x", "10",
        "-s", "10",
        "-d", output_dir,
        url,
    ]
    print(f"Downloading {url} to {output_dir}...")
    subprocess.run(command, check=True)

def extract_file(file_path):
    """Extract the specified .gz file."""
    command = ["gzip", "-d", file_path]
    print(f"Extracting {file_path}...")
    subprocess.run(command, check=True)

def main():
    parser = argparse.ArgumentParser(
        description="Download and extract the nucl_gb.accession2taxid.gz file."
    )
    parser.add_argument(
        "--url",
        default="https://ftp.ncbi.nih.gov/pub/taxonomy/accession2taxid/nucl_gb.accession2taxid.gz",
        help="URL to download the file. Default: NCBI nucl_gb.accession2taxid.gz",
    )
    parser.add_argument(
        "--output-dir",
        default="my_taxid",
        help="Output directory for the downloaded and extracted file. Default: 'my_taxid'",
    )

    args = parser.parse_args()

    # Create the output directory if it doesn't exist
    os.makedirs(args.output_dir, exist_ok=True)

    # Define the file paths
    gz_file_path = os.path.join(args.output_dir, os.path.basename(args.url))
    txt_file_path = gz_file_path.replace(".gz", "")

    # Download the file
    download_file(args.url, args.output_dir)

    # Extract the file
    extract_file(gz_file_path)

    print(f"File extracted to: {txt_file_path}")

if __name__ == "__main__":
    main()

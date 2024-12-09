#!/usr/bin/env python3

import os
import subprocess
import argparse
from tqdm import tqdm


__author__ = "Patricia Agudelo-Romero, PhD."


def download_with_progress(url, output_folder, output_file):
    """
    Download file using aria2c with a progress bar.
    
    Args:
        url (str): The URL to download.
        output_folder (str): The folder to save the downloaded file.
        output_file (str): The name of the output file without the .gz extension.
    """
    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Full output file path
    gzipped_file = os.path.join(output_folder, f"{output_file}.fasta.gz")
    
    # Run aria2c to download the file with multiple connections and no file allocation
    command = [
        "aria2c",
        "--file-allocation=none",  # No file allocation
        "-c",                      # Continue downloading if partially downloaded
        "-x", "10",                 # Number of connections per server
        "-s", "10",                 # Number of servers to use
        "-d", output_folder,       # Destination folder
        "-o", f"{output_file}.fasta.gz",  # Output file name with .gz extension
        url
    ]
    
    # Using aria2c to download the file
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Capture output and error messages
    stdout, stderr = process.communicate()

    # Check for errors
    if process.returncode != 0:
        print(f"Error during download: {stderr.decode()}")
        return None
    
    # If download is successful, print the output
    print(stdout.decode())
    
    # Ensure the file exists
    if not os.path.exists(gzipped_file):
        print(f"File not found: {gzipped_file}")
        return None
    
def decompress_file(gzipped_file):
    """
    Decompress the downloaded .fasta.gz file into .fasta.
    
    Args:
        gzipped_file (str): The path to the gzipped file.
    """
    if os.path.exists(gzipped_file):
        print(f"Decompressing {gzipped_file}...")
        subprocess.run(["gzip", "-d", gzipped_file], check=True)
        print(f"Decompression completed: {gzipped_file[:-3]}")

def main():
    # Argument parser setup
    parser = argparse.ArgumentParser(description="Download viral proteomes from UniProt using aria2.")
    parser.add_argument(
        "--db",
        required=True,
        choices=["swissprot", "trembl"],
        help="Specify the database: 'swissprot' or 'trembl'."
    )
    parser.add_argument(
        "--output-dir",
        default="./",  # Default to current directory
        help="Directory to save the downloaded files."
    )
    args = parser.parse_args()
    
    # Determine the URL based on the selected database
    if args.db == "swissprot":
        url = "https://rest.uniprot.org/uniprotkb/stream?compressed=true&format=fasta&query=%28virus%29+AND+%28reviewed%3Atrue%29"
        output_folder = "swissprot"
        output_file = "viral_proteomes_swissprot"
    elif args.db == "trembl":
        url = "https://rest.uniprot.org/uniprotkb/stream?compressed=true&format=fasta&query=%28virus%29+AND+%28reviewed%3Afalse%29"
        output_folder = "trembl"
        output_file = "viral_proteomes_trembl"
    
    # Download the file with progress
    gzipped_file = download_with_progress(url, output_folder, output_file)
    
    # If the download is successful, decompress the file
    if gzipped_file:
        decompress_file(gzipped_file)

if __name__ == "__main__":
    main()

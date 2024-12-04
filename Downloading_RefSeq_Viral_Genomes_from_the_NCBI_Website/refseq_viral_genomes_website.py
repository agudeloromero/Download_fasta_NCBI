#!/usr/bin/env python3

import os
import argparse
import subprocess
import glob


__author__ = "Patricia Agudelo-Romero, PhD."


def download_and_unzip(url, output_dir):
    """
    Step 1: Download a file using aria2c and unzip it.
    """
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"Downloading from {url}...")
    download_command = [
        "aria2c",
        "--file-allocation=none",
        "-c",
        "-x", "10",
        "-s", "10",
        "-d", output_dir,
        url
    ]
    subprocess.run(download_command, check=True)

    # Unzip the downloaded file(s)
    print("Unzipping downloaded files...")
    gz_files = glob.glob(os.path.join(output_dir, "*.gz"))
    for gz_file in gz_files:
        subprocess.run(["gzip", "-d", gz_file], check=True)

    # Identify the unzipped file
    fasta_files = glob.glob(os.path.join(output_dir, "*.fna")) + \
                  glob.glob(os.path.join(output_dir, "*.fasta")) + \
                  glob.glob(os.path.join(output_dir, "*.fa"))

    if not fasta_files:
        raise FileNotFoundError("No FASTA files found after unzipping.")

    return fasta_files[0]  # Return the first found FASTA file

def filter_duplicates(input_fasta):
    """
    Step 2: Filter duplicates using dedupe.sh and save results to a new file.
    """
    output_fasta = input_fasta.replace(".fna", "_filtered.fna").replace(".fasta", "_filtered.fasta").replace(".fa", "_filtered.fa")
    log_file = os.path.join(os.path.dirname(input_fasta), "dedupe.log")

    print(f"Filtering duplicates from {input_fasta}...")
    dedupe_command = [
        "dedupe.sh",
        f"-Xmx20g",
        f"in={input_fasta}",
        f"out={output_fasta}"
    ]
    
    with open(log_file, "w") as log:
        subprocess.run(dedupe_command, check=True, stdout=log, stderr=subprocess.STDOUT)

    return output_fasta

def main():
    parser = argparse.ArgumentParser(description="Download, unzip, and optionally filter duplicate FASTA sequences.")

    # Arguments
    parser.add_argument(
        "--url",
        default="https://ftp.ncbi.nlm.nih.gov/refseq/release/viral/viral.1.1.genomic.fna.gz",
        help="URL to download the FASTA file. Default: RefSeq Viral Genomes"
    )
    parser.add_argument(
        "--output-dir",
        default="my_output",
        help="Output directory for downloaded and processed files. Default: 'my_output'"
    )
    parser.add_argument(
        "--skip-deduplication",
        action="store_true",
        help="Skip the duplicate filtering step. Default: False (perform deduplication)."
    )
    parser.add_argument(
        "--remove-intermediate",
        action="store_true",
        help="Remove intermediate files after deduplication."
    )

    args = parser.parse_args()

    # Step 1: Download and unzip
    try:
        input_fasta = download_and_unzip(args.url, args.output_dir)
    except Exception as e:
        print(f"Error during download/unzipping: {e}")
        return

    # Step 2: Filter duplicates (if not skipped)
    if not args.skip_deduplication:
        try:
            filtered_fasta = filter_duplicates(input_fasta)
            print(f"Filtered FASTA file saved to: {filtered_fasta}")
            
            # Remove intermediate files if requested
            if args.remove_intermediate:
                print("Removing intermediate files...")
                if os.path.exists(input_fasta):
                    os.remove(input_fasta)
        except Exception as e:
            print(f"Error during duplicate filtering: {e}")
            return
    else:
        print(f"Duplicate filtering skipped. Original file is: {input_fasta}")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import os
import argparse
import subprocess
import glob
import shutil


__author__ = "Patricia Agudelo-Romero, PhD."


def download_viral_genomes(database, output_dir, parallel, assembly_levels="complete", formats="fasta", dry_run=False, metadata_table=None):
    """
    Download viral genomes using ncbi-genome-download with user-defined parameters.
    Process the downloaded files: unzip, concatenate, and clean up.
    
    Args:
        database (str): 'genbank' or 'refseq'.
        output_dir (str): Directory to save the downloaded genomes.
        parallel (int): Number of parallel processes for downloading.
        assembly_levels (str): Assembly level to download (default: 'complete').
        formats (str): File format to download (default: 'fasta').
        dry_run (bool): If True, perform a dry run without actual downloads.
        metadata_table (str): Path to save the metadata table (if specified).
    """
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"Downloading viral genomes from {database}...")

    # Build the ncbi-genome-download command
    command = [
        "ncbi-genome-download",
        "viral",
        "--assembly-levels", assembly_levels,
        "--formats", formats,
        "--progress-bar",
        "--parallel", str(parallel),
        "--section", database,
        "-o", output_dir
    ]

    # Add optional parameters
    if dry_run:
        command.append("--dry-run")
    if metadata_table:
        command.extend(["--metadata-table", metadata_table])

    # Run the command
    try:
        subprocess.run(command, check=True)
        print("Download completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during download: {e}")
        return

    if not dry_run:
        # Process downloaded files
        process_downloaded_files(output_dir, database)


def process_downloaded_files(output_dir, database):
    """
    Process the downloaded genome files: unzip, concatenate, and clean up.
    
    Args:
        output_dir (str): Directory where genomes are saved.
        database (str): Database used for downloading ('genbank' or 'refseq').
    """
    data_path = os.path.join(output_dir, database, "viral")
    if not os.path.exists(data_path):
        print(f"Error: Expected data path '{data_path}' not found.")
        return

    print("Unzipping .fna.gz files...")
    gz_files = glob.glob(os.path.join(data_path, "*", "*.fna.gz"))
    for gz_file in gz_files:
        subprocess.run(["gunzip", gz_file])

    print("Concatenating all .fna files...")
    fna_files = glob.glob(os.path.join(data_path, "*", "*.fna"))
    output_file = os.path.join(output_dir, f"viral_complete_genomes_{database}.fna")
    with open(output_file, "w") as outfile:
        for fna_file in fna_files:
            with open(fna_file, "r") as infile:
                outfile.write(infile.read())

    print(f"Concatenated genomes saved to: {output_file}")

    print("Cleaning up intermediate files...")
    shutil.rmtree(os.path.join(output_dir, database))

    print(f"Cleanup completed. All data saved in: {output_dir}")


if __name__ == "__main__":
    # Command-line argument parsing
    parser = argparse.ArgumentParser(description="Download and process viral genomes using ncbi-genome-download.")
    parser.add_argument(
        "-d", "--database", choices=["genbank", "refseq"], required=True,
        help="Database to search ('genbank' or 'refseq')."
    )
    parser.add_argument(
        "-o", "--output", default="out_complete",
        help="Output directory. Default is 'out_complete'."
    )
    parser.add_argument(
        "-p", "--parallel", type=int, default=6,
        help="Number of parallel downloads. Default is 6."
    )
    parser.add_argument(
        "--assembly-levels", default="complete",
        help="Assembly levels to download (e.g., 'complete', 'scaffold'). Default is 'complete'."
    )
    parser.add_argument(
        "--formats", default="fasta",
        help="File formats to download (default: 'fasta')."
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Perform a dry run without actual downloads."
    )
    parser.add_argument(
        "--metadata-table", type=str,
        help="Path to save the metadata table."
    )

    # Parse the command-line arguments
    args = parser.parse_args()

    # Execute the genome download function
    download_viral_genomes(
        database=args.database,
        output_dir=args.output,
        parallel=args.parallel,
        assembly_levels=args.assembly_levels,
        formats=args.formats,
        dry_run=args.dry_run,
        metadata_table=args.metadata_table
    )


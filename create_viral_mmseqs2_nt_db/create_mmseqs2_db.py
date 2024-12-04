#!/usr/bin/env python3

import os
import argparse
import subprocess


__author__ = "Patricia Agudelo-Romero, PhD."


def create_directory(directory):
    """Create a directory if it does not exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory {directory} created.")
    else:
        print(f"Directory {directory} already exists.")

def run_command(command):
    """Run a shell command and handle errors."""
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Successfully executed: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Error while executing: {command}")
        raise e

def main():
    parser = argparse.ArgumentParser(
        description="Create an MMseqs2 viral nucleotide database with taxonomy and taxid integration."
    )
    
    parser.add_argument(
        "--viral-fasta",
        type=str,
        required=True,
        help="Path to the viral multi-FASTA file (e.g., my_output/viral.1.1.genomic_filtered.fna)."
    )
    parser.add_argument(
        "--viral-taxid",
        type=str,
        required=True,
        help="Path to the viral taxid mapping file (e.g., my_taxid/viral.fna.taxidmapping)."
    )
    parser.add_argument(
        "--taxonomy-dir",
        type=str,
        required=True,
        help="Path to the taxonomy directory (e.g., TAX_nt/)."
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="MMSEQ_Viral_DB_nt",
        help="Directory to store the MMseqs2 viral nucleotide database. Default: MMSEQ_Viral_DB_nt."
    )
    
    args = parser.parse_args()

    # Create output directory
    create_directory(args.output_dir)

    # Step 1: Create MMseqs2 database
    db_command = f"mmseqs createdb {args.viral_fasta} {args.output_dir}/viral.nt.fnaDB"
    run_command(db_command)

    # Step 2: Add taxonomy and taxid to MMseqs2 database
    taxdb_command = (
        f"mmseqs createtaxdb {args.output_dir}/viral.nt.fnaDB tmp "
        f"--ncbi-tax-dump {args.taxonomy_dir} "
        f"--tax-mapping-file {args.viral_taxid}"
    )
    run_command(taxdb_command)

    print(f"MMseqs2 database created successfully in {args.output_dir}")

if __name__ == "__main__":
    main()

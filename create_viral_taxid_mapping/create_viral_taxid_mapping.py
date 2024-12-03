#!/usr/bin/env python3

import os
import argparse
import subprocess

"""
Patricia Agudelo-Romero, PhD.
"""

def create_output_dir(directory):
    """Ensure the output directory exists."""
    os.makedirs(directory, exist_ok=True)


def check_and_generate_taxidmap(taxid_file, taxidmap_file, col1, col2):
    """Check if taxidmapfile exists and create it if necessary."""
    if not os.path.isfile(taxidmap_file):
        print(f"Generating taxid map file from {taxid_file}...")
        command = f"sed '1d' {taxid_file} | awk '{{print ${col1} \" \" ${col2}}}' > {taxidmap_file}"
        subprocess.run(command, shell=True, check=True)


def create_blast_database(fasta_file, taxidmap_file, output_dir):
    """Create a BLAST database."""
    db_dir = os.path.join(output_dir, "DB_virus")
    os.makedirs(db_dir, exist_ok=True)
    print(f"Creating BLAST database in {db_dir}...")
    command = [
        "makeblastdb",
        "-in", fasta_file,
        "-dbtype", "nucl",
        "-parse_seqids",
        "-input_type", "fasta",
        "-taxid_map", taxidmap_file,
        "-title", "Viral_ncbi",
        "-out", os.path.join(db_dir, "Viral_ncbi"),
    ]
    subprocess.run(command, check=True)


def generate_taxid_mapping(db_dir, output_file):
    """Generate the taxid mapping file."""
    print(f"Generating taxid mapping file: {output_file}...")
    command = [
        "blastdbcmd",
        "-db", os.path.join(db_dir, "Viral_ncbi"),
        "-entry", "all",
        "-outfmt", "%a %T",
        "-out", output_file,
    ]
    subprocess.run(command, check=True)


def cleanup_intermediate_files(taxidmap_file, db_dir):
    """Remove intermediate files and directories."""
    print("Cleaning up intermediate files...")
    if os.path.isfile(taxidmap_file):
        os.remove(taxidmap_file)
    if os.path.isdir(db_dir):
        subprocess.run(["rm", "-r", db_dir], check=True)


def main():
    parser = argparse.ArgumentParser(
        description="Create viral taxid mapping file using BLAST tools."
    )
    parser.add_argument(
        "--taxid",
        required=True,
        help="Path to the taxid file (e.g., my_taxid/nucl_gb.accession2taxid).",
    )
    parser.add_argument(
        "--fasta",
        required=True,
        help="Path to the multi-FASTA file (e.g., my_output/viral.1.1.genomic_filtered.fna).",
    )
    parser.add_argument(
        "--output-dir",
        default=None,
        help="Output directory for the taxid mapping file. Default: same as the taxid file location.",
    )
    parser.add_argument(
        "--keep-intermediate",
        action="store_true",
        help="Keep intermediate files (taxidmapfile and DB_virus).",
    )
    parser.add_argument(
        "--col1",
        type=int,
        default=2,
        help="Column number for the first field in taxid map generation. Default: 2.",
    )
    parser.add_argument(
        "--col2",
        type=int,
        default=3,
        help="Column number for the second field in taxid map generation. Default: 3.",
    )

    args = parser.parse_args()

    # Define paths
    taxid_dir = os.path.dirname(args.taxid)
    output_dir = args.output_dir or taxid_dir
    create_output_dir(output_dir)
    taxidmap_file = os.path.join(output_dir, "taxidmapfile")
    db_dir = os.path.join(output_dir, "DB_virus")
    taxid_mapping_file = os.path.join(output_dir, "viral.fna.taxidmapping")

    # Steps
    check_and_generate_taxidmap(args.taxid, taxidmap_file, args.col1, args.col2)
    create_blast_database(args.fasta, taxidmap_file, output_dir)
    generate_taxid_mapping(db_dir, taxid_mapping_file)

    # Cleanup intermediate files if not keeping
    if not args.keep_intermediate:
        cleanup_intermediate_files(taxidmap_file, db_dir)

    print(f"Taxid mapping file created at: {taxid_mapping_file}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import os
import argparse
import pandas as pd
from tqdm import tqdm

__author__ = "Patricia Agudelo-Romero, PhD."


def filter_seq_ids(fasta_file, output_file):
    """
    Extract sequence IDs (e.g., NC_029989.1) from the headers of a multi-FASTA file.
    
    :param fasta_file: Path to the input multi-FASTA file.
    :param output_file: Path to save the extracted sequence IDs.
    """
    print("Filtering sequence IDs...")
    with open(fasta_file, 'r') as fasta, open(output_file, 'w') as output:
        total_lines = sum(1 for line in fasta)
        fasta.seek(0)  # Reset the file pointer
        with tqdm(total=total_lines, unit="line", ncols=100, desc="Filtering sequence IDs") as pbar:
            for line in fasta:
                if line.startswith(">"):
                    seq_id = line.split()[0][1:]  # Extract the sequence ID without ">"
                    output.write(seq_id + "\n")
                pbar.update(1)
    print(f"Sequence IDs saved to {output_file}.")


def filter_taxid_mapping(genbank_file, output_file, col1=1, col2=2, chunksize=100000):
    """
    Filter columns from a GenBank accession taxid file by reading in chunks using pandas.
    
    :param genbank_file: Path to the nucleotide GenBank accession taxid file.
    :param output_file: Path to save the taxid mapping file.
    :param col1: Column number for accession ID (default is 1).
    :param col2: Column number for taxid (default is 2).
    :param chunksize: The number of lines to read at a time.
    """
    print("Filtering taxid mapping using pandas (chunksize)...")
    try:
        # Read the file in chunks and filter columns
        chunk_iter = pd.read_csv(genbank_file, sep="\t", header=None, usecols=[col1-1, col2-1], chunksize=chunksize)

        with open(output_file, 'w') as output:
            for chunk in chunk_iter:
                # Write the filtered chunk to the output file
                chunk.to_csv(output, sep=" ", index=False, header=False, mode='a')
                output.flush()
        print(f"Taxid mapping file saved to {output_file}.")
    except Exception as e:
        print(f"Error while processing the file: {e}")
        raise


def create_taxid_mapping(seq_ids_file, filtered_taxid_mapping, output_file):
    """
    Filter rows in the filtered taxid mapping file to include only sequence IDs from seq_ids_file.

    :param seq_ids_file: Path to the file containing sequence IDs to retain.
    :param filtered_taxid_mapping: Path to the input taxid mapping file.
    :param output_file: Path to save the filtered taxid mapping file.
    """
    print("Filtering taxid mapping based on sequence IDs...")
    seq_id_set = set()
    with open(seq_ids_file, 'r') as seq_ids:
        seq_id_set = {seq_id.strip() for seq_id in seq_ids}
    
    total_lines = sum(1 for line in open(filtered_taxid_mapping))
    with open(filtered_taxid_mapping, 'r') as taxid_mapping, open(output_file, 'w') as output, tqdm(total=total_lines, unit="line", ncols=100, desc="Filtering taxid mapping") as pbar:
        for line in taxid_mapping:
            accession = line.split()[0]
            if accession in seq_id_set:
                output.write(line)
            pbar.update(1)
    print(f"Viral taxid mapping file saved to {output_file}.")


def main():
    parser = argparse.ArgumentParser(
        description="Create a viral taxid mapping file by filtering sequence IDs from a multi-FASTA file and mapping them to taxids from a GenBank accession taxid file."
    )
    
    parser.add_argument(
        "--fasta",
        type=str,
        required=True,
        help="Path to the input multi-FASTA file."
    )
    parser.add_argument(
        "--genbank-taxid",
        type=str,
        required=True,
        help="Path to the nucleotide GenBank accession taxid file."
    )
    parser.add_argument(
        "--output-seq-ids",
        type=str,
        default="viral_seq_ids.txt",
        help="Path to save the extracted sequence IDs. Default: viral_seq_ids.txt"
    )
    parser.add_argument(
        "--filtered-taxid-mapping",
        type=str,
        default="filtered_taxid_mapping.txt",
        help="Path to save the intermediate filtered taxid mapping file. Default: filtered_taxid_mapping.txt"
    )
    parser.add_argument(
        "--output-taxid-mapping",
        type=str,
        default="viral_taxid_mapping.txt",
        help="Path to save the final taxid mapping file. Default: viral_taxid_mapping.txt"
    )
    parser.add_argument(
        "--col1",
        type=int,
        default=2,
        help="Column number for accession ID in the GenBank file. Default: 2"
    )
    parser.add_argument(
        "--col2",
        type=int,
        default=3,
        help="Column number for taxid in the GenBank file. Default: 3"
    )
    parser.add_argument(
        "--save-intermediate",
        action="store_true",
        help="Save intermediate files instead of removing them."
    )
    args = parser.parse_args()

    # Step 1: Extract sequence IDs from the multi-FASTA file
    filter_seq_ids(args.fasta, args.output_seq_ids)

    # Step 2: Create taxid mapping file from GenBank accession taxid file using pandas with chunksize
    filter_taxid_mapping(args.genbank_taxid, args.filtered_taxid_mapping, args.col1, args.col2)

    # Step 3: Filter taxid mapping using sequence IDs
    create_taxid_mapping(args.output_seq_ids, args.filtered_taxid_mapping, args.output_taxid_mapping)

    # Remove intermediate files if not requested
    if not args.save_intermediate:
        print("Removing intermediate files...")
        os.remove(args.output_seq_ids)
        os.remove(args.filtered_taxid_mapping)
        print("Intermediate files removed.")
    else:
        print("Intermediate files retained.")


if __name__ == "__main__":
    main()


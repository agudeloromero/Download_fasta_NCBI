#!/usr/bin/env python3

import os
import argparse
import pandas as pd


__author__ = "Patricia Agudelo-Romero, PhD."


def parse_fasta_to_dataframe(file_path, output_file):
    """
    Parse a FASTA file and extract taxonomic IDs and sequence identifiers.

    :param file_path: Path to the input FASTA file.
    :param output_file: Path to the output TSV file.
    """
    rows = []
    with open(file_path, 'r') as fasta_file:
        for line in fasta_file:
            if line.startswith(">"):  # Process header lines
                parts = line.split('|')
                between_pipes = parts[1] if len(parts) > 1 else "N/A"  # Extract string between pipes
                
                ox_index = line.find("OX=")
                ox_string = line[ox_index + 3:].split()[0] if ox_index != -1 else "N/A"  # Extract "OX=" value
                
                rows.append([between_pipes, ox_string])  # Add to rows

    # Create DataFrame and save it
    df = pd.DataFrame(rows)
    os.makedirs(os.path.dirname(output_file), exist_ok=True)  # Ensure output directory exists
    df.to_csv(output_file, sep="\t", index=False, header=False)
    print(f"Output written to: {output_file}")


def main():
    """
    Main function to parse command-line arguments and process the FASTA file.
    """
    parser = argparse.ArgumentParser(
        description="Parse a FASTA file from Uniprot and extract sequence identifiers and taxonomic IDs."
    )
    parser.add_argument(
        "input_file",
        type=str,
        help="Path to the input FASTA file (.fasta, .fna, or .fa).",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="taxid_aa/taxid_aa.tsv",
        help="Path to the output file (default: taxid_aa/taxid_aa.tsv).",
    )

    args = parser.parse_args()

    # Validate input file
    if not os.path.isfile(args.input_file):
        print(f"Error: Input file '{args.input_file}' does not exist.")
        exit(1)

    if not args.input_file.endswith((".fasta", ".fna", ".fa")):
        print("Error: Input file must have a .fasta, .fna, or .fa extension.")
        exit(1)

    parse_fasta_to_dataframe(args.input_file, args.output)


if __name__ == "__main__":
    main()

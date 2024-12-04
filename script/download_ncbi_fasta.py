#!/usr/bin/env python3

import sys
import os
from Bio import Entrez


__author__ = "Patricia Agudelo-Romero, PhD."


def download_fasta(reference_id, email, output_folder):
    """
    Downloads a FASTA file from NCBI GenBank using a reference ID.

    Args:
        reference_id (str): The GenBank reference ID (e.g., NC_074663.1).
        email (str): Email address for NCBI API usage (required by NCBI).
        output_folder (str): Folder to save the downloaded FASTA.
    """
    Entrez.email = email  # Required by NCBI
    output_file = os.path.join(output_folder, f"{reference_id}.fasta")

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    try:
        print(f"Fetching FASTA for {reference_id}...")
        handle = Entrez.efetch(db="nucleotide", id=reference_id, rettype="fasta", retmode="text")
        fasta_data = handle.read()
        handle.close()

        # Save FASTA data to a file
        with open(output_file, 'w') as file:
            file.write(fasta_data)

        print(f"FASTA file saved to {output_file}")
    except Exception as e:
        print(f"Error fetching {reference_id}: {e}")

def process_input(input_path):
    """
    Reads reference IDs from a file or processes a single ID.

    Args:
        input_path (str): Path to a file containing IDs or a single ID string.

    Returns:
        list: A list of reference IDs to process.
    """
    if os.path.isfile(input_path):
        with open(input_path, 'r') as file:
            ids = [line.strip() for line in file if line.strip()]
        print(f"Loaded {len(ids)} IDs from {input_path}")
        return ids
    else:
        return [input_path]

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <input_path_or_id> <email> <output_folder>")
        sys.exit(1)

    input_path = sys.argv[1]
    email = sys.argv[2]
    output_folder = sys.argv[3]

    # Process the input to extract IDs
    reference_ids = process_input(input_path)

    # Download FASTA files for each ID
    for ref_id in reference_ids:
        download_fasta(ref_id, email, output_folder)

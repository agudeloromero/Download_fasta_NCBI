#!/usr/bin/env python3

import os
import argparse
import csv
import time
import random
from Bio import Entrez
from Bio import SeqIO

def fetch_genome_ids(query, email, batch_size=5000, max_retries=5):
    """
    Fetch genome IDs in smaller paginated batches to avoid timeouts.
    Patricia Agudelo-Romero, PhD.
    
    Args:
        query (str): Search query for NCBI.
        email (str): Email address for NCBI.
        batch_size (int): Number of results per batch.
        max_retries (int): Maximum retries for failed requests.
    Returns:
        list: List of genome IDs.
    """
    Entrez.email = email
    Entrez.timeout = 120
    genome_ids = []
    retstart = 0

    while True:
        try:
            print(f"Fetching batch starting at {retstart}...")
            search_handle = Entrez.esearch(
                db="nuccore",
                term=query,
                retmax=batch_size,
                retstart=retstart
            )
            search_results = Entrez.read(search_handle)
            search_handle.close()

            ids = search_results["IdList"]
            genome_ids.extend(ids)

            if len(ids) < batch_size:
                break  # No more results
            retstart += batch_size
            time.sleep(random.uniform(0.5, 2))  # Random delay
        except Exception as e:
            print(f"Error fetching genome IDs: {e}. Retrying...")
            max_retries -= 1
            if max_retries <= 0:
                raise RuntimeError("Exceeded maximum retries for genome ID fetch.")
            time.sleep(5)

    return genome_ids


def download_sequences(genome_ids, output_file):
    """
    Fetch and save genome sequences for a list of genome IDs.
    Patricia Agudelo-Romero, PhD.
    
    Args:
        genome_ids (list): List of genome IDs.
        output_file (str): File to save sequences.
    """
    print(f"Downloading sequences for {len(genome_ids)} genomes...")
    with open(output_file, "w") as out_f:
        for chunk in range(0, len(genome_ids), 500):
            try:
                chunk_ids = genome_ids[chunk:chunk + 500]
                fetch_handle = Entrez.efetch(
                    db="nuccore",
                    id=",".join(chunk_ids),
                    rettype="fasta",
                    retmode="text"
                )
                for record in SeqIO.parse(fetch_handle, "fasta"):
                    SeqIO.write(record, out_f, "fasta")
                fetch_handle.close()
                time.sleep(random.uniform(1, 3))  # Random delay
            except Exception as e:
                print(f"Error fetching sequences for chunk {chunk}: {e}. Retrying...")


def download_metadata(genome_ids, metadata_file):
    """
    Fetch and save metadata for a list of genome IDs.
    Patricia Agudelo-Romero, PhD.
    
    Args:
        genome_ids (list): List of genome IDs.
        metadata_file (str): File to save metadata.
    """
    print(f"Downloading metadata for {len(genome_ids)} genomes...")
    with open(metadata_file, "w", newline="") as csvfile:
        fieldnames = ["Accession", "Taxonomy ID", "Title", "Organism", "Length", "UpdateDate"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for chunk in range(0, len(genome_ids), 500):
            try:
                chunk_ids = genome_ids[chunk:chunk + 500]
                metadata_handle = Entrez.esummary(db="nuccore", id=",".join(chunk_ids))
                metadata_records = Entrez.read(metadata_handle)
                metadata_handle.close()

                for record in metadata_records:
                    writer.writerow({
                        "Accession": record.get("AccessionVersion", "N/A"),
                        "Taxonomy ID": record.get("TaxId", "N/A"),
                        "Title": record.get("Title", "N/A"),
                        "Organism": record.get("Organism", "N/A"),
                        "Length": record.get("Length", "N/A"),
                        "UpdateDate": record.get("UpdateDate", "N/A"),
                    })
                time.sleep(random.uniform(1, 3))  # Random delay
            except Exception as e:
                print(f"Error fetching metadata for chunk {chunk}: {e}. Retrying...")


def download_viral_genomes(taxonomic_ids, database, email, genome_type, output_dir):
    """
    Download viral genomes and metadata for specified taxonomic groups.
    Patricia Agudelo-Romero, PhD.
    
    Args:
        taxonomic_ids (dict): Dictionary of taxonomic groups and their IDs.
        database (str): 'genbank' or 'refseq'.
        email (str): Email address for NCBI.
        genome_type (str): Type of genome to search.
        output_dir (str): Directory to save downloaded data.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for group, taxon_id in taxonomic_ids.items():
        print(f"Processing {group} (TaxID: {taxon_id})...")
        base_query = f"txid{taxon_id}[Organism] AND {genome_type}[Title]"
        db_specific_query = f"{base_query} AND {database}[Filter]" if database == "refseq" else base_query

        genome_ids = fetch_genome_ids(db_specific_query, email)
        if not genome_ids:
            print(f"No genomes found for {group} (TaxID: {taxon_id}).")
            continue

        output_file = os.path.join(output_dir, f"{group}_{database}_genomes.fasta")
        metadata_file = os.path.join(output_dir, f"{group}_{database}_metadata.csv")

        download_sequences(genome_ids, output_file)
        download_metadata(genome_ids, metadata_file)


if __name__ == "__main__":
    taxonomic_ids = {
        "dsDnaViruses": "35237",
        "dsRnaViruses": "35325",
        "ssDnaViruses": "29258",
        "ssRnaViruses": "439488",
        "allViruses": "10239"
    }

    parser = argparse.ArgumentParser(description="Download viral genomes and metadata from NCBI.")
    parser.add_argument("-d", "--database", choices=["genbank", "refseq"], default="genbank")
    parser.add_argument("-e", "--email", required=True)
    parser.add_argument("-g", "--genome-type", default="complete genome")
    parser.add_argument("-o", "--output", default="genomes")
    args = parser.parse_args()

    download_viral_genomes(taxonomic_ids, args.database, args.email, args.genome_type, args.output)
  

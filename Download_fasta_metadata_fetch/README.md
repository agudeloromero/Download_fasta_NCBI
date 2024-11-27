# Download FASTA files and metadata from NCBI using esearch and fetch

This Python script downloads viral genomes in FASTA format from NCBI, as well as the metadata. It supports:
1. RefSeq database.
2. GenBank database.

## **Setup**

**1. Download the script from [here](https://github.com/agudeloromero/Download_fasta_NCBI/blob/main/Download_fasta_metadata_fetch/download_viral_genomes_metadata_NCBI_fetch.py) and give it execution permissions on your machine:**
```
chmod +x download_viral_genomes_metadata_NCBI_fetch.py
```

**2. Install Required Dependencies**

The script uses Python 3 and the following Python packages:

* biopython

* argparse

Install them using `pip` (or your environment's package manager):
```bash
pip install biopython argparse
```

**3. Prepare for Execution**
Make sure you have the following information ready:

NCBI Email Requirement: You must provide an email address as NCBI requires it to identify users for API access.

---

## **Run script:**

The script accepts several parameters, including the database (`genbank` or `refseq`), genome type (e.g., "complete genome"), and output directory.

**Example Commands**

For the `refseq` database:
```bash
./download_viral_genomes.py -d refseq -e user@example.com -g "complete genome" -o /path/to/output_directory
```

For the `genbank` database:
```bash
./download_viral_genomes.py -d genbank -e user@example.com -g "complete genome" -o /path/to/output_directory
```

---

## **Output:**

The script will create subdirectories and files based on the taxonomic groups defined in the script:

**1. For genomes:**

Fasta files for each group will be saved in the specified output directory. Example:
```bash
/dir/my_output/dsDnaViruses_genbank_genomes.fasta
```

**2. For Metadata:**

CSV files containing metadata for each group will be saved in the output directory. Example:
```bash
/dir/my_output/dsDnaViruses_genbank_metadata.csv
```

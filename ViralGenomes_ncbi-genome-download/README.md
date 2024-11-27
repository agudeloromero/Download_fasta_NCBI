# Download Viral Genomes FASTA files and metadata from NCBI using [ncbi-genome-download](https://github.com/kblin/ncbi-genome-download) tool

This Python script downloads viral genomes in FASTA format from NCBI, as well as the metadata. It supports:
1. RefSeq database.
2. GenBank database.

## **Setup:**

**1. Download the script from [here](https://github.com/agudeloromero/Download_fasta_NCBI/blob/main/ViralGenomes_ncbi-genome-download/PAR_ncbi-genome-download.py) and give it execution permissions on your machine:**
```bash
chmod +x PAR_ncbi-genome-download.py
```

**2. Install Required Dependencies**

The script uses Python 3.8 or later and the following Python packages. Required Python libraries:
* ncbi-genome-download
* argparse
* subprocess
* glob
* os
* shutil

Install them using `pip` (or your environment's package manager):
``` bash
pip install ncbi-genome-download argparse glob os shutil
```

## **Run script:**

The script accepts several parameters such as database, output directory, and the number of parallel downloads. The script automatically handles unzipping and concatenation of the multiple FASTA files into a single multi-FASTA file.

**Example Commands**

For the `refseq` database:
```bash
./PAR_ncbi-genome-download.py -d refseq -o /dir/output_directory -p 6
```

For the `genbank` database:
```bash
./PAR_ncbi-genome-download.py -d genbank -o /dir/output_directory -p 6
```

## **Output:**

The script will create a multi FASTA files with all the viral sequences:

**1. For genomes:**

Fasta files for each group will be saved in the specified output directory. Example:
```bash
/dir/output_directory/viral_complete_genomes_{database}.fna
```

**2. For Metadata:**

CSV files containing metadata for each group will be saved in the output directory. Example:
```bash
/dir/output_directory/viral_complete_genomes_metadata_{database}.tsv
```

## **Post-Processing Steps (Handled by the Script)**

The script performs the following preprocessing steps after downloading:

**1. Unzipping:**
Extracts all `.fna.gz` files in the `output_directory`.

**2. Concatenation:**
Combines all `.fna` files into a single multi-FASTA file for each database.

**3. Cleanup:**

Removes intermediate files and directories to save space.

Example Output Directory Structure (Post-Execution):
```
output_directory/
  viral_complete_genomes_refseq.fna
output_directory/
  viral_complete_genomes_genbank.fna
```

## **Notes and Troubleshooting:**

* NCBI API Rate-Limiting: If you encounter download issues due to rate limits, try reducing the --parallel value or adding a delay between requests (customization required).

* Testing Dry Run: Use --dry-run to preview what the script would download.

For any unexpected errors, refer to the script’s printed logs for debugging information or update ncbi-genome-download.


## **Parameters:**

| **Parameter**         | **Description**                                                                                 | **Example**               |
|------------------------|-------------------------------------------------------------------------------------------------|---------------------------|
| `-d`, `--database`     | Database to query: `genbank` or `refseq`. Default is `refseq`.                                  | `-d genbank`              |
| `-o`, `--output`       | Output directory for the processed genomes. Default is `out_complete`.                         | `-o output_directory`     |
| `-p`, `--parallel`     | Number of parallel downloads. Default is 4.                                                    | `-p 6`                    |
| `--assembly-levels`    | Specify assembly levels: `complete` (default), `scaffold`, etc.                                | `--assembly-levels complete` |
| `--formats`            | File format to download. Default is `fasta`.                                                   | `--formats fasta`         |
| `--retries`            | Number of retry attempts in case of download failure. Default is 4.                            | `--retries 3`             |
| `--dry-run`            | Preview the download process without actually downloading.                                      | `--dry-run`               |
| `--metadata-table`     | Save metadata to the specified table.                                                          | `--metadata-table mytable.csv` |

For more information run help.
```bash
./PAR_ncbi-genome-download.py --help
usage: download_viral_genomes.py [-h] -d {genbank,refseq} [-o OUTPUT] [-p PARALLEL] [--assembly-levels ASSEMBLY_LEVELS] [--formats FORMATS] [--dry-run] [--metadata-table METADATA_TABLE]

Download and process viral genomes using ncbi-genome-download.

optional arguments:
  -h, --help            show this help message and exit
  -d {genbank,refseq}, --database {genbank,refseq}
                        Database to search ('genbank' or 'refseq').
  -o OUTPUT, --output OUTPUT
                        Output directory. Default is 'out_complete'.
  -p PARALLEL, --parallel PARALLEL
                        Number of parallel downloads. Default is 6.
  --assembly-levels ASSEMBLY_LEVELS
                        Assembly levels to download (e.g., 'complete', 'scaffold'). Default is 'complete'.
  --formats FORMATS     File formats to download (default: 'fasta').
  --dry-run             Perform a dry run without actual downloads.
  --metadata-table METADATA_TABLE
                        Path to save the metadata table.
```


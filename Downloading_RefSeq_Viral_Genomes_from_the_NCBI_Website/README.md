# Downloading_RefSeq_Viral_Genomes_from_the_NCBI_Website

This Python script downloads the RefSeq viral genomes FASTA file [viral.1.1.genomic.fna.gz](https://ftp.ncbi.nlm.nih.gov/refseq/release/viral/viral.1.1.genomic.fna.gz) from [NCBI website](https://ftp.ncbi.nlm.nih.gov/refseq/release/viral/). It has two main streams:
1. Download RefSeq viral genomes.
2. Optinal deduplication step.

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

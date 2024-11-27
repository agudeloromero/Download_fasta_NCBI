# Download FASTA files from NCBI with an ID

This Python script downloads GenBank FASTA files. It supports:
1. Downloading a single reference ID.
2. Downloading multiple references from a file.

## **Setup**

**1. Download the script from [here](https://github.com/agudeloromero/Download_fasta_NCBI/blob/main/Download_fasta_with_ID/download_ncbi_fasta.py) and give it execution permissions on your machine:**
```
chmod +x download_ncbi_fasta.py
```

**2. Install Required Dependencies**

The script uses Python 3 and the following Python packages:

* biopython


Install them using `pip` (or your environment's package manager):
``` bash
pip install biopython
```

**3. NCBI Email Requirement**

You must provide an email address as NCBI requires it to identify users for API access.


## **Examples**

**(1) Single reference**

To download a single reference FASTA:
```
python download_ncbi_fasta.py NC_074663.1 user@example.com output_folder
```

**(2) Multiple references**

Create a text file (ie ids.txt) with one ID per line, like this:
```
NC_029066.1
NC_002484.2
NC_030929.1
```

## **Run script:**

```
python download_ncbi_fasta.py ids.txt user@example.com output_folder
```


## **Output:**

Fasta files will be saved in the specified folder (in this case output_folder), with filenames corresponding to the reference IDs.
```
ll output_folder
NC_029066.1.fasta
NC_002484.2.fasta
NC_030929.1.fasta
```


# Creating Viral Taxid Mapping with `create_viral_taxid_mapping_from_files2.py`

This Python script automates the process of creating a viral taxid mapping file by filtering sequence IDs from a multi-FASTA file and mapping them to taxids from a nucleotide GenBank taxid file. The script uses `Dask` for efficient large-file processing and supports chunk-wise reading with `pandas`.

**Features**

* Extracts sequence IDs from the headers of a multi-FASTA file.
* Filters specific columns from a GenBank taxid file for accession and taxid mapping.
* Matches sequence IDs to their corresponding taxids.
* Offers options for customizing column numbers and saving intermediate files.

---

## **Setup**

### 1. Download the Script

Download the script from [here](https://github.com/agudeloromero/Download_fasta_NCBI/blob/main/create_viral_taxid_mapping_from_files/create_viral_taxid_mapping_from_files.py) or clone the repository and navigate to the directory:
```bash
git clone https://github.com/agudeloromero/Download_fasta_NCBI.git
cd Download_fasta_NCBI/create_viral_taxid_mapping_files
chmod +x create_viral_taxid_mapping_from_files.py
```

### 2. Install Dependencies

Create and Activate a Conda Environment

Use the provided [`TaxidMapping_fromFiles_env.yml`](https://github.com/agudeloromero/Download_fasta_NCBI/blob/main/create_viral_taxid_mapping_from_files/TaxidMapping_fromFiles_env.yml) file to set up your environment.

1. Create the Environment

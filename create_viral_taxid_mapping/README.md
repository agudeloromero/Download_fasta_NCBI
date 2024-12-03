# Creating Viral Taxid Mapping with BLAST Tools

This Python script automates the process of creating a viral taxid mapping file from the genbank taxid file. It builds a BLAST database with the viral multi-FASTA file and matchs the taxid present in the database, and generates a mapping file by filtering it for the viral sequence accessions to taxids.

**Features**

* Verifies and generates a viral taxid map from the input taxid file.
* Creates a BLAST database from the provided multi-FASTA file.
* Generates a taxid mapping file in the desired output directory.
* Cleans up intermediate files by default, with an option to keep them.

---

## **Setup**

### 1. Download the Script

Clone the repository and navigate to the appropriate directory:
```bash
git clone https://github.com/agudeloromero/Download_fasta_NCBI.git
cd Download_fasta_NCBI/Create_Viral_Taxid_Mapping
chmod +x create_viral_taxid_mapping.py
```

## 2. Install Dependencies
**Create and Activate a Conda Environment**

Use the provided `TaxidMapping_env.yml` file to set up your environment.

**1. Create the Environment**
```bash
conda env create -f TaxidMapping_env.yml
```

**2. Activate the Environment**
```bash
conda activate TaxidMapping_env
```

## Run the Script
**1. Basic Usage**
Run the script with default settings:
```bash
./create_viral_taxid_mapping.py --taxid my_taxid/nucl_gb.accession2taxid --fasta my_output/viral.1.1.genomic_filtered.fna
```
This creates the taxid mapping file in the same directory as the input taxid file.

## 2. Custom Usage Examples

**Example 1: Specify Output Directory**
```bash
./create_viral_taxid_mapping.py --taxid my_taxid/nucl_gb.accession2taxid --fasta my_output/viral.1.1.genomic_filtered.fna --output-dir custom_output
```

**Example 2: Custom Taxid Columns**
```bash
./create_viral_taxid_mapping.py --taxid my_taxid/nucl_gb.accession2taxid --fasta my_output/viral.1.1.genomic_filtered.fna --col1 1 --col2 2
```

**Example 3: Keep Intermediate Files**
```bash
./create_viral_taxid_mapping.py --taxid my_taxid/nucl_gb.accession2taxid --fasta my_output/viral.1.1.genomic_filtered.fna --keep-intermediate
```

## Help

Run the script with `--help` to see all available options:
```bash
./create_viral_taxid_mapping.py --help
```

## Acknowledgments

* This script uses the BLAST+ suite for database creation and mapping.
* The taxid mapping generation is facilitated by standard UNIX tools `sed` and `awk`.

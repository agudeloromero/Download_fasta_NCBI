# Creating Viral Taxid Mapping with BLAST Tools

This Python script automates the process of creating a viral taxid mapping file from a GenBank taxid file. It builds a BLAST database using a viral multi-FASTA file, matches the taxids present in the database, and generates a mapping file linking viral sequence accessions to their corresponding taxids.

**Features**

* Verifies and generates a viral taxid map from the input taxid file.
* Creates a BLAST database from the provided multi-FASTA file.
* Generates a taxid mapping file in the desired output directory.
* Cleans up intermediate files by default, with an option to keep them.

---

## **Setup**

### 1. Download the Script

Download the script [here](https://github.com/agudeloromero/Download_fasta_NCBI/blob/main/create_viral_taxid_mapping/create_viral_taxid_mapping.py) or clone the repository and navigate to the appropriate directory:
```bash
git clone https://github.com/agudeloromero/Download_fasta_NCBI.git
cd Download_fasta_NCBI/Create_Viral_Taxid_Mapping
chmod +x create_viral_taxid_mapping.py
```

## 2. Install Dependencies
**Create and Activate a Conda Environment**

Use the provided [`TaxidMapping_env.yml`](https://github.com/agudeloromero/Download_fasta_NCBI/blob/main/create_viral_taxid_mapping/TaxidMapping_env.yml) file to set up your environment.

**1. Create the Environment**
```bash
conda env create -f TaxidMapping_env.yml
```

**2. Activate the Environment**
```bash
conda activate TaxidMapping_env
```

## Input Example

This is the nucleotide GenBank taxid file [nucl_gb.accession2taxid](https://ftp.ncbi.nih.gov/pub/taxonomy/accession2taxid/).
```bash
head my_taxid/nucl_gb.accession2taxid
accession       accession.version       taxid   gi
A00001  A00001.1        10641   58418
A00002  A00002.1        9913    2
A00003  A00003.1        9913    3
A00004  A00004.1        32630   57971
A00005  A00005.1        32630   57972
A00006  A00006.1        32630   57973
A00008  A00008.1        32630   57974
A00009  A00009.1        32630   57975
A00010  A00010.1        32630   57976
```
For an automate script check [download_nucleotide_genbank_taxid](https://github.com/agudeloromero/Download_fasta_NCBI/blob/main/download_nucleotide_genbank_taxid/README.md) repository.

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

## Example output my_taxid/viral.fna.taxidmapping
```bash
head my_taxid/viral.fna.taxidmapping 
NC_023309.1 1436892
NC_023310.1 1436892
NC_023303.1 1436892
NC_023311.1 1436892
NC_027026.1 1280920
NC_027016.1 1667587
NC_027040.1 44560
NC_027054.1 1156769
NC_023312.1 1303385
NC_026942.1 1634381
```

## Help

Run the script with `--help` to see all available options:
```bash
./create_viral_taxid_mapping.py --help
```

Help Menu:
```
usage: create_viral_taxid_mapping.py [-h] --taxid TAXID --fasta FASTA [--output-dir OUTPUT_DIR] [--keep-intermediate]
                                     [--col1 COL1] [--col2 COL2]

Create viral taxid mapping file using BLAST tools.

optional arguments:
  -h, --help            show this help message and exit
  --taxid TAXID         Path to the taxid file (e.g., my_taxid/nucl_gb.accession2taxid).
  --fasta FASTA         Path to the multi-FASTA file (e.g., my_output/viral.1.1.genomic_filtered.fna).
  --output-dir OUTPUT_DIR
                        Output directory for the taxid mapping file. Default: same as the taxid file location.
  --keep-intermediate   Keep intermediate files (taxidmapfile and DB_virus).
  --col1 COL1           Column number for the first field in taxid map generation. Default: 2.
  --col2 COL2           Column number for the second field in taxid map generation. Default: 3.
```

## Contributing

Contributions and feedback are welcome! If you encounter issues or have feature requests, feel free to open an issue in the [repository](https://github.com/agudeloromero/Download_fasta_NCBI/issues).

## Acknowledgments

* This script uses the [BLAST+](https://anaconda.org/bioconda/blast) suite from [Miniconda](https://docs.anaconda.com/miniconda/) for database creation and mapping.
* The taxid mapping generation is facilitated by standard UNIX tools `sed` and `awk`.

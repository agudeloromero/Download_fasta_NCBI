# Creating Viral Taxid Mapping using the viral multi-FASTA and the nucleotide GenBank taxid file `nucl_gb.accession2taxid` files.

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

**Create and activate the Environment:**
```bash
conda env create -f TaxidMapping_fromFiles_env.yml
conda activate TaxidMapping_fromFiles_env
```

---

### Input Example

**1. GenBank Taxid File**

Example: [nucl_gb.accession2taxid](https://ftp.ncbi.nih.gov/pub/taxonomy/accession2taxid/) file.
```bash
head nucl_gb.accession2taxid
accession       accession.version       taxid   gi
A00001  A00001.1        10641   58418
A00002  A00002.1        9913    2
A00003  A00003.1        9913    3
A00004  A00004.1        32630   57971
A00005  A00005.1        32630   57972
```
There is an automate script to download this file in the repository [`download_nucleotide_genbank_taxid`](https://github.com/agudeloromero/Download_fasta_NCBI/blob/main/download_nucleotide_genbank_taxid/README.md)

**2. Multi-FASTA File**

Provide a file with sequences of interest:
```bash
head viral_sequences.fasta
>NC_000001.11 Homo sapiens chromosome 1, GRCh38.p13 Primary Assembly
GATTACA...
>NC_000002.12 Homo sapiens chromosome 2, GRCh38.p13 Primary Assembly
TACGGTA...
```
There is an automate script to download this file in the repository [`Downloading_RefSeq_Viral_Genomes_from_the_NCBI_Website`](https://github.com/agudeloromero/Download_fasta_NCBI/tree/main/Downloading_RefSeq_Viral_Genomes_from_the_NCBI_Website)

### Running the Script

**1. Basic Usage**

Run the script with default settings:
```bash
./create_viral_taxid_mapping_from_files.py --fasta viral_sequences.fasta --genbank-taxid nucl_gb.accession2taxid
```
This extracts sequence IDs, maps them to taxids, and generates the final mapping file in the default locations.

### 2. Custom Usage Examples

**Example 1: Specify Output Files**
```bash
./create_viral_taxid_mapping_from_files.py \
    --fasta viral_sequences.fasta \
    --genbank-taxid nucl_gb.accession2taxid \
    --output-taxid-mapping viral_taxid_mapping.txt
```

**Example 2: Change Columns**

In case that the input is a costume file, there is the opportunity to changes the columns (Default 2 and 3)
```bash
./create_viral_taxid_mapping_from_files.py \
    --fasta viral_sequences.fasta \
    --genbank-taxid nucl_gb.accession2taxid \
    --col1 1 --col2 2
```

**Example 3: Keep Intermediate Files**
```bash
./create_viral_taxid_mapping_from_files.py \
    --fasta viral_sequences.fasta \
    --genbank-taxid nucl_gb.accession2taxid \
    --output-taxid-mapping viral_taxid_mapping.txt \
    --save-intermediate \
    --output-seq-ids seq_ids.txt \
    --filtered-taxid-mapping filtered_mapping.txt \
```

### Output Example

**Final Mapping File**
```bash
head viral_taxid_mapping.txt
NC_000001.11 9606
NC_000002.12 9606
NC_000003.12 9606
```

### Help

Run the script with `--help` for all options:
```bash
./create_viral_taxid_mapping_from_files2.py --help
```

**Help Menu**
```plaintext
usage: create_viral_taxid_mapping_from_files2.py [-h] --fasta FASTA --genbank-taxid GENBANK_TAXID
                                                 [--output-seq-ids OUTPUT_SEQ_IDS]
                                                 [--filtered-taxid-mapping FILTERED_TAXID_MAPPING]
                                                 [--output-taxid-mapping OUTPUT_TAXID_MAPPING]
                                                 [--col1 COL1] [--col2 COL2] [--save-intermediate]

Filter sequence IDs and map taxids using FASTA and GenBank files.

optional arguments:
  -h, --help            show this help message and exit
  --fasta FASTA         Input multi-FASTA file.
  --genbank-taxid GENBANK_TAXID
                        GenBank accession taxid file.
  --output-seq-ids OUTPUT_SEQ_IDS
                        File to save sequence IDs (default: viral_seq_ids.txt).
  --filtered-taxid-mapping FILTERED_TAXID_MAPPING
                        Intermediate filtered taxid mapping file (default: filtered_taxid_mapping.txt).
  --output-taxid-mapping OUTPUT_TAXID_MAPPING
                        Final taxid mapping file (default: viral_taxid_mapping.txt).
  --col1 COL1           Column number for accession ID (default: 2).
  --col2 COL2           Column number for taxid (default: 3).
  --save-intermediate   Keep intermediate files.
```

### Contributing

Contributions and feedback are welcome! Report issues or request features in the [repository](https://github.com/agudeloromero/Download_fasta_NCBI/issues).

### Acknowledgments

* [`Dask`](https://www.dask.org) enables efficient parallel processing of large files.
  
  Rocklin, M. (2015). Dask: Parallel computation with blocked algorithms and task scheduling. In Proceedings of the 14th python in science conference.
  
* [`pandas`](https://pandas.pydata.org) provides chunk-wise file handling for memory-efficient processing.

McKinney, W., & others. (2010). Data structures for statistical computing in python. In Proceedings of the 9th Python in Science Conference (Vol. 445, pp. 51–56).

* The script is designed for scalable workflows in bioinformatics.


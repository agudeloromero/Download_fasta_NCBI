# Creating MMseqs2 Viral Nucleotide Database with Taxonomy Integration

This Python script [(`create_mmseqs2_db.py`)](https://github.com/agudeloromero/Download_fasta_NCBI/blob/main/create_viral_mmseqs2_nt_db/create_mmseqs2_db.py) automates the creation of an MMseqs2 viral nucleotide database, integrates taxonomy data, and applies taxid mapping for taxonomic classification analysis.

## Features

* Automates the creation of an MMseqs2 database from viral multi-FASTA files.
* Integrates taxonomy and taxid mapping for enhanced analysis.
* Ensures the output directory is created if it doesn't exist.

## Setup

Environment Installation

Save the following YAML file as [`MMSeqs2_env.yml`](https://github.com/agudeloromero/Download_fasta_NCBI/blob/main/create_viral_mmseqs2_nt_db/MMSeqs2_env.yml):
```yaml
name: MMSeqs2_env
channels:
  - bioconda
  - conda-forge
dependencies:
  - python>=3.9
  - mmseqs2
```

Steps to Create the Environment:
```bash
conda env create -f MMSeqs2_env.yml
conda activate MMSeqs2_env
```

**Input Files**

* Viral multi-FASTA file: `dir/viral.1.1.genomic_filtered.fna`.
* Viral taxid mapping file: `dir/viral.fna.taxidmapping`.
* NCBI taxonomy nucleotide directory path: `dir/TAX_nt`.


## Usage

**Basic Usage**

Basic Command:
```bash
./create_mmseqs2_db.py --viral-fasta my_output/viral.1.1.genomic_filtered.fna \
                       --viral-taxid my_taxid/viral.fna.taxidmapping \
                       --taxonomy-dir TAX_nt
```
It is important to keep default folder name is the aim is to run the database for [EVEREST_nf](https://github.com/agudeloromero/everest_nf).

Output Structure:
```bash
tree MMSEQ_Viral_DB_nt/
MMSEQ_Viral_DB_nt/
├── viral.nt.fnaDB
├── viral.nt.fnaDB.dbtype
├── viral.nt.fnaDB.index
├── viral.nt.fnaDB.lookup
├── viral.nt.fnaDB.source
├── viral.nt.fnaDB_h
├── viral.nt.fnaDB_h.dbtype
├── viral.nt.fnaDB_h.index
├── viral.nt.fnaDB_mapping
└── viral.nt.fnaDB_taxonomy
```

**Custom Output Directory**

Specify an output directory:
```bash
./create_mmseqs2_db.py --viral-fasta my_output/viral.1.1.genomic_filtered.fna \
                       --viral-taxid my_taxid/viral.fna.taxidmapping \
                       --taxonomy-dir TAX_nt \
                       --output-dir Custom_DB
```

Output Structure:
```bash
tree Custom_DB/
Custom_DB/
├── viral.nt.fnaDB
├── viral.nt.fnaDB.dbtype
├── viral.nt.fnaDB.index
├── viral.nt.fnaDB.lookup
├── viral.nt.fnaDB.source
├── viral.nt.fnaDB_h
├── viral.nt.fnaDB_h.dbtype
├── viral.nt.fnaDB_h.index
├── viral.nt.fnaDB_mapping
└── viral.nt.fnaDB_taxonomy
```


## Help Menu

Run the script with the `--help` flag to see available options:
```
./create_mmseqs2_db.py --help
```

Help Output:
```plaintext
usage: create_mmseqs2_db.py [-h] --viral-fasta VIRAL_FASTA --viral-taxid VIRAL_TAXID --taxonomy-dir TAXONOMY_DIR
                            [--output-dir OUTPUT_DIR] [--keep-intermediate]

Create an MMseqs2 viral nucleotide database with taxonomy and taxid integration.

optional arguments:
  -h, --help            show this help message and exit
  --viral-fasta VIRAL_FASTA
                        Path to the viral multi-FASTA file (e.g., my_output/viral.1.1.genomic_filtered.fna).
  --viral-taxid VIRAL_TAXID
                        Path to the viral taxid mapping file (e.g., my_taxid/viral.fna.taxidmapping).
  --taxonomy-dir TAXONOMY_DIR
                        Path to the taxonomy directory (e.g., TAX_nt/).
  --output-dir OUTPUT_DIR
                        Directory to store the MMseqs2 viral nucleotide database. Default: MMSEQ_Viral_DB_nt.
```



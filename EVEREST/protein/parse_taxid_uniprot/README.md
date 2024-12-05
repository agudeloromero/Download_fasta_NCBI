# Extracting Taxonomic IDs from UniProt FASTA Files with `parse_taxid_uniprot.py`

This Python script processes UniProt-formatted multi-FASTA files to extract sequence identifiers and their corresponding taxonomic IDs (`OX` fields). It generates a tab-separated values (TSV) output file containing this mapping, with customizable output paths and support for default file handling.

### Features

* Extracts sequence identifiers and taxonomic IDs (`OX`) from FASTA headers.
* Supports FASTA file extensions: `.fasta`, `.fna`, `.fa`.
* Automatically creates output directories if needed.
* Allows users to specify custom output file paths.
* Includes a `--help` option for usage guidance.

### Setup

**1. Download the Script**

Clone the repository and navigate to the directory:
```bash
git clone [https://github.com/<your-repo>/parse-taxid-uniprot.git](https://github.com/agudeloromero/Download_fasta_NCBI/edit/main/EVEREST/protein/parse_taxid_uniprot.git)
cd parse-taxid-uniprot
chmod +x parse_taxid_uniprot.py
```

**2. Install Dependencies**

Create a Conda environment using the provided YAML file:

Create and activate the environment:
```bash
conda env create -f taxid_aa.yml
conda activate taxid_aa
```

Environment File (taxid_aa.yml):
```yaml
name: taxid_aa
channels:
  - conda-forge
dependencies:
  - python=3.9
  - pandas
```

### Input/Output Example

**Input FASTA File**

The input must be a FASTA file with headers containing the OX field.
```plaintext
>tr|A0A023H4K0|A0A023H4K0_9FLAV Genome polyprotein OS=dengue virus type 2 OX=11060 PE=4 SV=1
...
>tr|A0A023H4L2|A0A023H4L2_9FLAV Genome polyprotein OS=dengue virus type 2 OX=11060 PE=4 SV=1
...
>tr|A0A023H573|A0A023H573_9FLAV Genome polyprotein OS=dengue virus type 2 OX=11060 PE=4 SV=1
...
```
**Output tsv File**

Output Example
The output is a TSV file with two columns: sequence identifier and taxonomic ID:
```plaintext
A0A023H4K0    11060
A0A023H4L2    11060
A0A023H573    11060
```

### Usage

**1. Default**

Run the script with the input file only:
```bash
./parse_taxid_uniprot.py dir/file.fasta
```

Default output:
```plaintext
taxid_aa/
└── taxid_aa.tsv
```

**2. Custom**

Specify a custom output path:
```bash
./parse_taxid_uniprot.py dir/file.fasta --output dir/custom_output.tsv
Custom output:
```

Custom output:
```bash
dir/
└── custom_output.tsv
```

### 3. Help Menu

Use the `--help` option to view all usage instructions:
```bash
./parse_taxid_uniprot.py --help
```

Help Output:
```plaintext
usage: parse_taxid_uniprot.py [-h] [--output OUTPUT] input_file

Parse a FASTA file from UniProt and extract sequence identifiers and taxonomic IDs.

positional arguments:
  input_file      Path to the input FASTA file (.fasta, .fna, or .fa).

optional arguments:
  -h, --help      Show this help message and exit.
  --output OUTPUT Path to the output file (default: taxid_aa/taxid_aa.tsv).
```

### Contributing

Contributions and feedback are welcome! Report issues or request features in the [repository](https://github.com/agudeloromero/Download_fasta_NCBI/issues).

### Acknowledgments
  
* [pandas](https://pandas.pydata.org) provides efficient data handling and TSV file generation.

McKinney, W., & others. (2010). Data structures for statistical computing in python. In Proceedings of the 9th Python in Science Conference (Vol. 445, pp. 51–56).








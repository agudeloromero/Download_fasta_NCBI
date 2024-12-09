# UniProt Viral Proteomes Downloader

## Overview

This Python script allows users to download viral proteomes from the UniProt database using `aria2c` for efficient downloading. The script supports both the Swiss-Prot and TrEMBL databases, automates the decompression of `.gz` files, and ensures robust error handling.

## Features
- Downloads viral proteomes from UniProt in `.fasta.gz` format using `aria2c`.
- Supports two databases:
  - **Swiss-Prot**: Curated protein sequences.
  - **TrEMBL**: Computationally annotated protein sequences.
- Decompresses downloaded `.gz` files to `.fasta` format.
- Creates output folders specific to the database type (`swissprot` or `trembl`).

## Requirements
- **Python 3.x**
- **aria2c** installed and available in your system's PATH.
- **gzip** for decompression.

## Installation
Clone this repository and navigate to the script directory:
```bash
git clone https://github.com/agudeloromero/Download_fasta_NCBI.git
cd Download_fasta_NCBI/EVEREST/protein/download_uniprot_virus/
```

**Install necessary dependencies:**
```bash
pip install argparse aria2
```

## Usage

Run the script with the --db parameter to specify the database type:
```bash
python download_uniprot_virus_aria.py --db <database>
```

**Parameters**
* `--db`: Database type to download. Options:
* `swissprot`: Curated database.
* `trembl`: Computationally annotated database.

## Example

Download viral proteomes from the Swiss-Prot database:
```bash
python download_uniprot_virus_aria.py --db swissprot
```

Download viral proteomes from the TrEMBL database:
```bash
python download_uniprot_virus_aria.py --db trembl
```

### Output

* The downloaded `.gz` file is saved in the respective database folder (`swissprot` or `trembl`).
* The `.gz` file is automatically decompressed into `.fasta` format.

**Example Output Structure**

After running for Swiss-Prot:
```bash
swissprot/
├── viral_proteomes_swissprot.fasta
```

For TrEMBL:
```bash
trembl/
├── viral_proteomes_trembl.fasta
```

### Troubleshooting

* Command Not Found: Ensure 'aria2c' is installed.
* Incomplete File: If the download is interrupted, the script supports resuming.
* Permissions Error: Ensure the script has write access to the output directory.


## Help

Run the script with `--help` to see all available options:
```bash
./download_uniprot_virus.py --help
```

Help Menu:
```bash

## Help

Run the script with `--help` to see all available options:
```bash
./download_uniprot_virus.py --help
```

Help Menu:
```bash
usage: download_uniprot_virus.py [-h] --db {swissprot,trembl} [--output-dir OUTPUT_DIR]

Download viral proteomes from UniProt using aria2.

optional arguments:
  -h, --help            show this help message and exit
  --db {swissprot,trembl}
                        Specify the database: 'swissprot' or 'trembl'.
  --output-dir OUTPUT_DIR
                        Directory to save the downloaded files.

```

## Contributing

Contributions and feedback are welcome! If you encounter issues or have feature requests, feel free to open an issue in the [repository](https://github.com/agudeloromero/Download_fasta_NCBI/issues).

## Acknowledgments

This script uses the [aria2c](https://github.com/aria2/aria2) tool for efficient file downloads.


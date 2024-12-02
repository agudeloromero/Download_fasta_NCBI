# Downloading NCBI nucl_gb.accession2taxid.gz File

This Python script automates the download and extraction of the `nucl_gb.accession2taxid.gz` file from the [NCBI FTP website](https://ftp.ncbi.nih.gov/pub/taxonomy/accession2taxid/). 

**Features**

* Downloads the `nucl_gb.accession2taxid.gz` file using `aria2c`.
* Extracts the file into a specified directory.
* Supports customization of the download URL and output directory.

---

## **Setup**

### 1. Download the Script

Clone the repository and navigate to the appropriate directory:
```bash
git clone https://github.com/agudeloromero/Download_fasta_NCBI.git
cd Download_fasta_NCBI/Downloading_NCBI_Nucl_GB_TaxID
chmod +x download_nucl_gb_taxid.py
```

### 1. Install Dependencies

Create and Activate a Conda Environment

Use the provided `NuclGBTaxID_env.yml` file to set up your environment.

**1. Create the Environment**
```bash
conda env create -f NuclGBTaxID_env.yml
```

**2. Activate the Environment**
```bash
conda activate NuclGBTaxID_env
```

**Tools and Libraries**

*aria2c: For efficient file downloads (installed via pip in the YAML file).
*Standard Python Libraries: Modules like `os`, `argparse`, and `subprocess` are included in Python's standard library and do not require additional installation.

## Run the Script

**1. Basic Usage**

Run the script with default settings:
```bash
./download_nucl_gb_taxid.py
```

This downloads and extracts the `nucl_gb.accession2taxid.gz` file into the default directory `my_taxid`.

Default Output:
```bash
tree my_taxid/
my_taxid/
└── nucl_gb.accession2taxid
```

## 2. Custom Usage Examples

**Example 1: Specify Output Directory**

Save the extracted data to a custom directory:
```bash
./download_nucl_gb_taxid.py --output-dir custom_taxid
```

Output:
```bash
tree custom_taxid/
custom_taxid/
└── nucl_gb.accession2taxid
```

## Example 2: Custom Download URL

Download a file from a custom URL:
```bash
./download_nucl_gb_taxid.py --url ftp://example.com/custom_file.gz --output-dir custom_data
```

Output:
```bash
tree custom_data/
custom_data/
└── custom_file
```

## Help

Run the script with `--help` to see all available options:
```bash
./download_nucl_gb_taxid.py --help
```

Help Menu:
```bash
usage: download_nucl_gb_taxid.py [-h] [--url URL] [--output-dir OUTPUT_DIR]

Download and extract the nucl_gb.accession2taxid.gz file.

optional arguments:
  -h, --help            Show this help message and exit.
  --url URL             URL to download the file. Default: NCBI nucl_gb.accession2taxid.gz
  --output-dir OUTPUT_DIR
                        Output directory for the downloaded and extracted file. Default: 'my_taxid'.
```

## Contributing

Contributions and feedback are welcome! If you encounter issues or have feature requests, feel free to open an issue in the [repository](https://github.com/agudeloromero/Download_fasta_NCBI/issues).

## Acknowledgments

This script uses the [aria2c](https://github.com/aria2/aria2) tool for efficient file downloads.

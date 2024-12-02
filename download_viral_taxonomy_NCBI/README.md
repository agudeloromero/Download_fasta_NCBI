# Downloading NCBI Taxonomy Data from the FTP Website

This Python script automates the download and extraction of the NCBI taxonomy dump from the FTP website. The taxonomy data is available as a tarball (`taxdump.tar.gz`) containing multiple files, which can be used for taxonomy-related analyses.

**Features**

* Automatically downloads the taxonomy tarball file.
* Extracts the contents into a specified directory.
* Removes the original `.tar.gz` file after extraction.
* Allows customization of the download URL and output directory.

---

## **Setup**

### 1. Download the Script

Download the script from [here](https://github.com/agudeloromero/Download_fasta_NCBI/blob/main/download_viral_taxonomy_NCBI/download_viral_tax_NCBI.py) or Clone the repository and navigate to the appropriate directory:
```bash
git clone https://github.com/agudeloromero/Download_fasta_NCBI.git
cd Download_fasta_NCBI/Downloading_NCBI_Taxonomy
chmod +x download_ncbi_taxonomy.py
```

### 1. Install Dependencies

Create and Activate a Conda Environment

Use the provided NCBI_Taxonomy_env.yml file to set up your environment.

This script uses Python 3.9 or later. Use the provided [NCBI_Taxonomy_env.yml](https://github.com/agudeloromero/Download_fasta_NCBI/blob/main/download_viral_taxonomy_NCBI/NCBI_Taxonomy_env.yml) file to set up your environment.

**1. Create the Environment**
```bash
conda env create -f NCBI_Taxonomy_env.yml
```

**2. Activate the Environment**
```bash
conda activate NCBI_Taxonomy_env
```

**Tools and Libraries**

* aria2c: For efficient file downloads (installed via pip in the YAML file).
* Standard Python Libraries: Modules like `os`, `argparse`, and `subprocess` are included in Python's standard library and do not require additional installation.

## Run the Script

**1. Basic Usage**
Run the script with default settings:
```bash
./download_ncbi_taxonomy.py
```
This downloads the `taxdump.tar.gz` file, extracts its contents into a default directory (`TAX_nt`), and removes the tarball after extraction.

**Default Output:**
```bash
tree TAX_nt/
TAX_nt/
├── citations.dmp
├── delnodes.dmp
├── division.dmp
├── gc.prt
├── gencode.dmp
├── merged.dmp
├── names.dmp
├── nodes.dmp
```

##2. Custom Usage Examples

**Example 1: Specify Output Directory**

Save the extracted data to a custom directory:
```bash
./download_ncbi_taxonomy.py --output-dir my_taxonomy_data
``

Output:
```bash
tree my_taxonomy_data/
my_taxonomy_data/
├── citations.dmp
├── delnodes.dmp
├── division.dmp
├── gc.prt
├── gencode.dmp
├── merged.dmp
├── names.dmp
├── nodes.dmp
```

### Example 2: Custom Download URL
Download a tarball from a custom URL:
```bash
./download_ncbi_taxonomy.py --url ftp://example.com/my_taxonomy.tar.gz --output-dir custom_dir
```

Output:
```bash
tree custom_dir/
custom_dir/
├── citations.dmp
├── delnodes.dmp
├── division.dmp
├── gc.prt
├── gencode.dmp
├── merged.dmp
├── names.dmp
├── nodes.dmp
```

## Help

Run the script with --help to see all available options:
```bash
./download_ncbi_taxonomy.py --help
```

Help Menu:
```
usage: download_ncbi_taxonomy.py [-h] [--url URL] [--output-dir OUTPUT_DIR]

Download and extract the NCBI taxonomy dump.

optional arguments:
  -h, --help            Show this help message and exit.
  --url URL             URL to download the taxonomy dump. Default: NCBI taxonomy dump URL.
  --output-dir OUTPUT_DIR
                        Output directory for downloaded and extracted files. Default: 'TAX_nt'.
```

## Contributing

Contributions and feedback are welcome! If you encounter issues or have feature requests, feel free to open an issue in the [repository](https://github.com/agudeloromero/Download_fasta_NCBI/issues).

## Acknowledgments

This script uses the [aria2c](https://github.com/aria2/aria2) tool for efficient file downloads.



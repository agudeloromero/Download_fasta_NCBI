# Downloading_RefSeq_Viral_Genomes_from_the_NCBI_Website

This Python script automates the download of RefSeq viral genomes in FASTA format [(viral.1.1.genomic.fna.gz)](https://ftp.ncbi.nlm.nih.gov/refseq/release/viral/viral.1.1.genomic.fna.gz) from the [NCBI website](https://ftp.ncbi.nlm.nih.gov/refseq/release/viral/). It offers two main functionalities:
1. Download RefSeq viral genomes.
2. Optional deduplication of sequences to remove duplicates from the downloaded multi-FASTA file.

**Features**

* Automatically downloads the viral genome file.
* Unzips and processes the downloaded file.
* Optionally filters duplicate FASTA sequences using bbmap's dedupe.sh.
*  Supports customization of the download URL and output directory.
* Generates a log file (dedupe.log) during deduplication.
* Offers the option to clean up intermediate files.

## **Setup:**

**1. Download the script from [here](https://github.com/agudeloromero/Download_fasta_NCBI/blob/main/Downloading_RefSeq_Viral_Genomes_from_the_NCBI_Website/refseq_viral_genomes_website.py) or clone it from this repository, then give it execution permissions on your machine:**
```bash
git clone https://github.com/agudeloromero/Download_fasta_NCBI.git
cd Download_fasta_NCBI/Downloading_RefSeq_Viral_Genomes_from_the_NCBI_Website
chmod +x refseq_viral_genomes_website.py
```

## 2. Install Dependencies

**Create and Activate a Conda Environment**

The script uses Python 3.9 or later. Use the provided [`RefSeq_env.yml`](https://github.com/agudeloromero/Download_fasta_NCBI/blob/main/Downloading_RefSeq_Viral_Genomes_from_the_NCBI_Website/RefSeq_env.yml) file to set up your environment.

**1. Create a Conda Environment:**
``` bash
conda env create -f RefSeq_env.yml
```

**2. Activate the Environment:**
``` bash
conda activate RefSeq_env
```

**Tools and Libraries**

* aria2c: For fast and efficient file downloads.
* bbmap: For deduplication of multi-FASTA files.
* Standard Python Libraries: Modules like `os`, `argparse`, `subprocess`, and `glob` are included in Python's standard library and do not require installation.

## **Run script:**

**1. Basic Usage**

Run the script with default settings:
```bash
./refseq_viral_genomes_website.py
```
This downloads, unzips, and deduplicates the RefSeq viral genome file. The results are saved in a default directory named my_output.

Default Output:
```bash
tree my_output
my_output/
├── dedupe.log
├── viral.1.1.genomic.fna
└── viral.1.1.genomic_filtered.fna
```

---

**2. Custom Usage Examples**

**Example 1: Specify Output Directory**
Save results in a custom directory and remove intermediate files:
```
./refseq_viral_genomes_website.py --output-dir my_refseq --remove-intermediate
```

Output:
```bash
tree my_refseq/
my_refseq/
├── dedupe.log
└── viral.1.1.genomic_filtered.fna
```

---

**Example 2: Custom Download URL**
Download and process a custom file:
```bash
./refseq_viral_genomes_website.py --url https://example.com/myfile.fna.gz --output-dir my_data --remove-intermediate
```

Output:
```bash
tree my_data/
my_data/
├── dedupe.log
└── myfile_filtered.fna
```

---

**Example 3: Skip Deduplication**
If you do not want to perform deduplication:
```bash
./refseq_viral_genomes_website.py --skip-deduplication
```

Output:
```bash
tree my_data/
my_data/
└── viral.1.1.genomic.fna
```

## **Help:**

Run the script with --help to see all available options:
```bash
./refseq_viral_genomes_website.py --help
```

Help Menu:
```plaintext
usage: refseq_viral_genomes_website.py [-h] [--url URL] [--output-dir OUTPUT_DIR] [--skip-deduplication] [--remove-intermediate]

Download, unzip, and optionally filter duplicate FASTA sequences.

optional arguments:
  -h, --help            show this help message and exit
  --url URL             URL to download the FASTA file. Default: RefSeq Viral Genomes
  --output-dir OUTPUT_DIR
                        Output directory for downloaded and processed files. Default: 'my_output'
  --skip-deduplication  Skip the duplicate filtering step. Default: False (perform deduplication).
  --remove-intermediate
                        Remove intermediate files after deduplication.
```

## Contributing

Contributions and feedback are welcome! If you encounter issues or have feature requests, feel free to open an issue in the [repository](https://github.com/agudeloromero/Download_fasta_NCBI/issues).

## Acknowledgments

* This script uses the [aria2c](https://github.com/aria2/aria2) tool for efficient file downloads.
* Sequence deduplication is powered by the [bbmap](https://github.com/BioInfoTools/BBMap/blob/master/README.md) suite.

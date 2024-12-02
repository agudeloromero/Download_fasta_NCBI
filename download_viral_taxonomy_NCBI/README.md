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

Clone the repository and navigate to the appropriate directory:
```bash
git clone https://github.com/agudeloromero/Download_fasta_NCBI.git
cd Download_fasta_NCBI/Downloading_NCBI_Taxonomy
chmod +x download_ncbi_taxonomy.py
```


# Downloading_RefSeq_Viral_Genomes_from_the_NCBI_Website

This Python script downloads the RefSeq viral genomes FASTA file [viral.1.1.genomic.fna.gz](https://ftp.ncbi.nlm.nih.gov/refseq/release/viral/viral.1.1.genomic.fna.gz) from [NCBI website](https://ftp.ncbi.nlm.nih.gov/refseq/release/viral/). It has two main streams:
1. Download RefSeq viral genomes.
2. Optinal deduplication step.

## **Setup:**

**1. Download the script from [here](https://github.com/agudeloromero/Download_fasta_NCBI/blob/main/Downloading_RefSeq_Viral_Genomes_from_the_NCBI_Website/refseq_viral_genomes_website.py) and give it execution permissions on your machine:**
```bash
chmod +x refseq_viral_genomes_website.py
```

**2. Install Required Dependencies**

The script uses Python 3.9 or later and the following Python packages. You can save the [RefSeq_env.yml file](https://github.com/agudeloromero/Download_fasta_NCBI/blob/main/Downloading_RefSeq_Viral_Genomes_from_the_NCBI_Website/RefSeq_env.yml) in your environment and then:.

**Create a Conda Environment:**
``` bash
conda env create -f RefSeq_env.yml
```

**Activate the Environment:**
``` bash
conda activate RefSeq_env
```

**Notes**

* The `aria2` and `bbmap tools` will be installed via `conda`.

* Packages like `os`, `argparse`, `subprocess`, and `glob` are part of Python's standard library and don’t need to be installed via `pip`. They are listed in the `RefSeq_env.yml` file for documentation purposes only.

## **Run script:**
Basic:
```
./refseq_viral_genomes_website.py
```

output:
```
tree my_output
my_output/
├── dedupe.log
├── viral.1.1.genomic.fna
└── viral.1.1.genomic_filtered.fna
```

Customise:
```
./refseq_viral_genomes_website.py --output-dir my_refseq --remove-intermediate
```

output:
```
tree my_refseq/
my_refseq/
├── dedupe.log
└── viral.1.1.genomic_filtered.fna
```

# Download FASTA files from NCBI

This Python script downloads GenBank FASTA files. It supports:
1. Downloading a single reference ID.
2. Downloading multiple references from a file.

**Setup**

Download the script from [here](https://github.com/agudeloromero/Download_fasta_NCBI/blob/main/script/download_ncbi_fasta.py) and give it execuation permissions on your machine:
```
chmod +x download_ncbi_fasta.py
```

---

**Examples**

**(1) Single reference**

To download a single reference FASTA:
```
python download_ncbi_fasta.py NC_074663.1 user@example.com output_folder
```

**(2) Multiple references**

Create a textfile (ie ids.txt) with one ID per line, like this:
```
NC_074663.1
NC_002695.1
NC_000913.3
```

---

**Run script:**

```
python download_ncbi_fasta.py ids.txt user@example.com output_folder
```

---

**Output:**

Fasta files will be saved in the specified folder (in this case output_folder), with filenames corresponding to the reference IDs.
```
ls output_folder
#NC_074663.1.fasta
#NC_002695.1.fasta
#NC_000913.3.fasta
```



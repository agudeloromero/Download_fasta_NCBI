# Download fasta files from NCBI
Python script for downloading GenBank fasta files. It can be used for (1) downloading a single reference or (2) multiple ones.

**Download [here](https://github.com/agudeloromero/Download_fasta_NCBI/blob/main/script/download_ncbi_fasta.py) and give permissions**
```
chmod +x download_ncbi_fasta.py
```

**Examples**
(1) Single reference
```
python download_ncbi_fasta.py NC_074663.1 user@example.com output_folder
```

(2) Multiple references
The script is designed to read one ID per line, as it is show below.
```
cat ids.txt
#NC_074663.1
#NC_002695.1
#NC_000913.3
```

**Run script:***
```
python download_ncbi_fasta.py ids.txt user@example.com output_folder
```

**Output:***
Fasta files will be saved in the specified folder, in this case output_folder, using the filenames of the reference.
```
ls output_folder
#NC_074663.1.fasta
#NC_002695.1.fasta
#NC_000913.3.fasta
```



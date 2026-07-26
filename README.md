# FASTA ANALYZER 

A python-based bioinformatics tool for analyzing DNA sequences in FASTA format using Biopython.

## Features 

- Count total sequences
- Find the longest sequence
- Find the shortest sequence
- Calculate the highest GC content
- Calculate the lowest GC content 
- Find the average length of the sequence
- Accept user input for the FASTA filename
- Handle missing file errors

## Requirements

- python 3
- Biopython

Install Biopython
```bash 
pip install biopython 
```

## How to run

```bash
python fasta_analyzer.py
```

Enter FASTA filename when prompted.

Example:

```text
Enter Fasta filename:
ls_orchid.fasta
```

## Sample Output

```text 
========================================
       FASTA ANALYZER
========================================

File Name             : ls_orchid.fasta

Total Sequences       : 94

Longest ID            : gi|2765620|emb|Z78495.1|PEZ78495
Longest Length        : 789 bp

Shortest ID           : gi|2765606|emb|Z78481.1|PIZ78481
Shortest Length       : 572 bp

Highest GC ID         : gi|2765658|emb|Z78533.1|CIZ78533
Highest GC Percentage : 59.59%

Lowest GC ID          : gi|2765587|emb|Z78462.1|PSZ78462
Lowest GC Percentage  : 32.34%

Average Length        : 718.28 bp

========================================
```

## Technologies used
- Python
- Biopython
- FASTA format

## Project Idea

FASTA is one of the most widely used file formats in bioinformatics for storing biological sequence data. 
This project demonstrates how Python and Biopython’s `SeqIO` module can be used to perform fundamental sequence analysis tasks, such as sequence counting, length analysis, GC content calculation and summary, statistics. 

## Author

Sakshi Shah

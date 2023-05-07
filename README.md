# sav2csv
Converts a SAV file (acronim of System for Analysis of Variables, originally created to be read by IBM SPSS Statistics) into a CSV file.

## Requirements
1. Python 3.7 or higher.
2. Install pyreadstat library with PIP running:
`pip install pyreadstat`
3. Make sure you have writing privileges in the destination folder.

## Running
Running `python sav2csv.py my_file.sav` will return a file called `my_file.csv` in the same directory.

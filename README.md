Excel Data Deduplication Scripts
Overview
This project includes Python scripts for detecting and managing duplicate entries in Excel files based on text similarity. The scripts leverage the fuzzywuzzy Python library to compare text fields and identify duplicates that exceed a specified similarity threshold.

Features
Single File Deduplication: levenshtein.py processes a single Excel file, identifies duplicates, marks them, and produces a cleaned file without duplicates.
Multiple File Deduplication: levenshtein-many-files.py processes multiple Excel files within a directory, merges them, and identifies duplicates across all files.
Prerequisites
Python 3.x
pandas: pip install pandas
fuzzywuzzy: pip install fuzzywuzzy
python-Levenshtein (optional for fuzzywuzzy efficiency): pip install python-Levenshtein
openpyxl: pip install openpyxl
Installation
Clone this repository or download the scripts directly into your project directory.

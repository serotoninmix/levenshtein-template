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

bash
Copy code
git clone https://github.com/yourusername/your-repository-name.git
cd your-repository-name
Usage
Single File Processing
Place your Excel file in the ./data directory.
Ensure your Excel file has the proper column names as expected by the script.
Run levenshtein.py:
bash
Copy code
python levenshtein.py
Processed files will be saved in the ./data directory with markings for duplicates and a cleaned file named processed_data_with_marks.xlsx.
Multiple Files Processing
Place all your Excel files in the ./data directory.
Ensure all Excel files are structured similarly and contain the necessary columns.
Run levenshtein-many-files.py:
bash
Copy code
python levenshtein-many-files.py
The script will generate unique_data.xlsx with unique records and duplicates_data.xlsx with a list of detected duplicates.
Contributing
Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.
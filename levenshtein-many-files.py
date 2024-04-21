import os
import pandas as pd
from fuzzywuzzy import fuzz

directory = './data'
excel_files = [f for f in os.listdir(directory) if f.endswith('.xlsx')]

def is_similar(string1, string2, threshold=85):
    string1 = str(string1)
    string2 = str(string2)
    return fuzz.ratio(string1, string2) > threshold

combined_df = pd.DataFrame()
source_files = {} 

for file in excel_files:
    df = pd.read_excel(os.path.join(directory, file), engine='openpyxl')
    current_length = len(combined_df)
    combined_df = pd.concat([combined_df, df], ignore_index=True)
    for i in range(current_length, len(combined_df)):
        source_files[i] = file

unique_rows = []
duplicates_list = []

for i in range(len(combined_df)):
    duplicate_found = False
    for j in range(i+1, len(combined_df)):
        similar_text = is_similar(combined_df.iloc[i]['text'], combined_df.iloc[j]['text'])
        similar_fetishes = is_similar(combined_df.iloc[i]['fetishes'], combined_df.iloc[j]['fetishes'])
        
        if similar_text and similar_fetishes:
            duplicates_list.append((combined_df.iloc[j]['fetishes'], source_files[j]))
            duplicate_found = True
            break
            
    if not duplicate_found:
        unique_rows.append(combined_df.iloc[i].values)

unique_df = pd.DataFrame(unique_rows, columns=combined_df.columns)
duplicates_df = pd.DataFrame(duplicates_list, columns=['Fetish', 'Source File'])  

unique_df.to_excel('unique_data.xlsx', index=False, engine='openpyxl')
duplicates_df.to_excel('duplicates_data.xlsx', index=False, engine='openpyxl')

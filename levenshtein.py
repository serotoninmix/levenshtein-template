import pandas as pd
from fuzzywuzzy import fuzz

def is_similar(string1, string2, threshold=85):
    string1 = str(string1).lower()
    string2 = str(string2).lower() 
    return fuzz.ratio(string1, string2) > threshold

df = pd.read_excel('./data/data.xlsx', engine='openpyxl')

fetishes = df[df.columns[0]]

marked_as_duplicate = set()

for i in range(len(fetishes)):
    if i in marked_as_duplicate:
        continue

    for j in range(i+1, len(fetishes)):
        if is_similar(fetishes[i], fetishes[j]):
            marked_as_duplicate.add(j)

df['Is_Duplicate'] = ['Yes' if i in marked_as_duplicate else 'No' for i in range(len(df))]

df.to_excel('./data/processed_data_with_marks.xlsx', index=False, engine='openpyxl')

unique_df = df[df['Is_Duplicate'] == 'No'].drop(columns=[df.columns[0], 'Is_Duplicate'])
unique_df[df.columns[0]] = fetishes

unique_df.to_excel('./data/data.xlsx', index=False, engine='openpyxl')

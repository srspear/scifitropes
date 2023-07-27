#...
#I used the following prompt with ChatGPT to generate this code:
#I need a python script that looks at the directory above where it sits and then combines each of the csv files in that directory together based on common columns. The same script then dedupes the list by removing rows whose "URL" column's value contains a duplicate of a previous row's "URL" value. The script then needs to save the output to a new csv file named "mainscifiworkstropesdb.csv" that sits in the same folder as the other csvs.
#...

import os
import pandas as pd
import glob

# Path to the directory above
parent_dir = os.path.dirname(os.getcwd())

# Get list of all CSV files in the parent directory
csv_files = glob.glob(os.path.join(parent_dir, "*.csv"))

# Initialize an empty DataFrame
df_combined = pd.DataFrame()

# Loop through each CSV file
for file in csv_files:
    # Read each CSV file and append it to the combined DataFrame
    df_combined = df_combined.append(pd.read_csv(file))

# Remove duplicate rows based on the "URL" column
df_combined.drop_duplicates(subset='URL', keep='first', inplace=True)

# Save the DataFrame to a new CSV file in the parent directory
df_combined.to_csv(os.path.join(parent_dir, 'mainscifiworkstropesdb.csv'), index=False)


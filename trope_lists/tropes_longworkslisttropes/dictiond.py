import os
import pandas as pd

# Loop through subdirectories and apply operation to each CSV file
root_dir = '/home/simeon/Documents/futuretropes2/scrapybranch/media_longtropelistworks/'  # replace with your root directory
for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".csv"):
            file_path = subdir + os.sep + file
            df = pd.read_csv(file_path)
            # Check if 'text' and 'url' columns exist in the dataframe
            if 'text' in df.columns and 'url' in df.columns:
                # Concatenate the 'text' and 'url' columns to form a string that looks like 'value A':'value B'
                df['concatenated'] = "'" + df['text'].astype(str) + "':'" + df['url'].astype(str) + "'"
                # Fill NaN values with an empty string
                df['concatenated'] = df['concatenated'].fillna('')
                # Join all the values in the 'concatenated' column to form a dictionary-like string
                dictionary_string = '{' + ', '.join(df['concatenated']) + '}'
                # Append the dictionary-like string as a new row
                df = df.append(pd.Series([dictionary_string], index=['concatenated']), ignore_index=True)
                # Write the modified data to a new CSV file with '_modified' appended to the original filename
                new_file_path = file_path.rsplit('.', 1)[0] + '_dictiond.csv'
                df.to_csv(new_file_path, index=False)


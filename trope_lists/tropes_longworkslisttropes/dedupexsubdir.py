import os
import pandas as pd

# Loop through subdirectories and apply operation to each CSV file
root_dir = '/home/simeon/Documents/futuretropes2/scrapybranch/media_longtropelistworks/'  # replace with your root directory
for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".csv"):
            file_path = subdir + os.sep + file
            df = pd.read_csv(file_path)
            # Check if 'url' column exists in the dataframe
            if 'url' in df.columns:
                # Deduplicate based on 'url' column
                df = df.drop_duplicates(subset='url')
                # Write the modified data to a new CSV file with '_modified' appended to the original filename
                new_file_path = file_path.rsplit('.', 1)[0] + '_deduped.csv'
                df.to_csv(new_file_path, index=False)

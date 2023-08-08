import os
import pandas as pd

# Load CSV files into pandas DataFrames
df2 = pd.read_csv('blacklisturls.csv')  # assuming this is your blacklist

# Loop through subdirectories and apply operation to each CSV file
root_dir = '/home/simeon/Documents/futuretropes2/scrapybranch/media_longtropelistworks/'  # replace with your root directory
for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".csv"):
            file_path = subdir + os.sep + file
            df1 = pd.read_csv(file_path)
            # Filter out URLs that exist in the blacklist
            df1 = df1[~df1['url'].isin(df2['url'])]
            # Write the filtered data to a new CSV file with '_filtered' appended to the original filename
            new_file_path = file_path.rsplit('.', 1)[0] + '_filtered.csv'
            df1.to_csv(new_file_path, index=False)


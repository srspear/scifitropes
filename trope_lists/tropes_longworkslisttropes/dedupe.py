import pandas as pd

# Load the CSV file
df = pd.read_csv('blacklisturls.csv')

# Drop duplicates
df = df.drop_duplicates()

# Save the DataFrame to a new CSV file
df.to_csv('blacklisturlsdeduped.csv', index=False)


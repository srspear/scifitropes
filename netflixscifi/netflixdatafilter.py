import pandas as pd

def filter_spreadsheet(baseline_path, target_path, output_path, baseline_is_excel=True, target_is_excel=True):
    # Load the baseline data (Excel or CSV)
    if baseline_is_excel:
        df_baseline = pd.read_excel(baseline_path)
    else:
        df_baseline = pd.read_csv(baseline_path)

    # Load the target data (Excel or CSV)
    if target_is_excel:
        df_target = pd.read_excel(target_path)
    else:
        df_target = pd.read_csv(target_path)

    # Extract titles from the baseline spreadsheet
    titles = df_baseline.iloc[:, 0].tolist()

    # Function to check if the title in target matches any in baseline
    def matches_any_title(s):
        for title in titles:
            if s.startswith(title):
                return True
        return False

    # Apply the function to filter the target DataFrame
    filtered_df = df_target[df_target.iloc[:, 0].apply(matches_any_title)]

    # Save the filtered DataFrame to a new file
    filtered_df.to_excel(output_path, index=False)  # Replace with to_csv for CSV

# Specify the paths to your files and their types
path_to_baseline_spreadsheet = 'mainscifiworksdb.csv'  # Update this path
baseline_is_excel = False  # Set to False if the baseline file is a CSV
path_to_target_spreadsheet = 'What_We_Watched_A_Netflix_Engagement_Report_2023Jan-Jun.xlsx'    # Update this path
target_is_excel = True   # Set to False if the target file is a CSV
path_to_output_spreadsheet = 'filtered_netflix_output.xlsx'          # Update this path

# Run the filtering process
filter_spreadsheet(path_to_baseline_spreadsheet, path_to_target_spreadsheet, path_to_output_spreadsheet, baseline_is_excel, target_is_excel)

print("Filtering complete. The results are saved in", path_to_output_spreadsheet)


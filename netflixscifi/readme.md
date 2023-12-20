
# Data Source

Part of the data used in this project originates from the "What We Watched: A Netflix Engagement Report," which can be found at [Netflix's Official Site](https://about.netflix.com/en/news/what-we-watched-a-netflix-engagement-report).

## Usage

Before running the script, ensure you have `pandas` installed in your Python environment. You can install it using pip:

```bash
pip install pandas
```

To use the script, specify the paths to your baseline and target spreadsheets, as well as the output path for the filtered data. Update the following variables in the script accordingly:

```python
path_to_baseline_spreadsheet = 'path/to/your/baseline.xlsx'
baseline_is_excel = True  # Set to False if the baseline file is a CSV
path_to_target_spreadsheet = 'path/to/your/target.xlsx'
target_is_excel = True    # Set to False if the target file is a CSV
path_to_output_spreadsheet = 'path/to/your/output.xlsx'
```

Run the script to filter the target spreadsheet based on the baseline spreadsheet data.

import pandas as pd
import openpyxl

##1. Save each state sheet from the excel file as a separate csv

# Read the Excel file
xls = pd.ExcelFile(input_excel_file)

# Get the sheet names
sheet_names = xls.sheet_names

# Iterate through each sheet and export to CSV
for sheet_name in sheet_names:
    # Read the sheet into a DataFrame
    df = pd.read_excel(input_excel_file, sheet_name)

    # Define the output CSV file name
    output_csv_file = f"{sheet_name}.csv"

    # Export the DataFrame to CSV
    df.to_csv(output_csv_file, index=False)

    print(f"Sheet '{sheet_name}' exported to '{output_csv_file}'")




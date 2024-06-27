import pandas as pd
import openpyxl
import os

wd = 'F:\\github\\birds_vis\\'

# 1. Save each state sheet from the excel file as a separate csv
## Read the Excel file
xls = pd.ExcelFile(f'{wd}02_SoIB_2023_main.xlsx')
## Create subfolder to store state csv files
os.makedirs(f'{wd}state_wise\\', exist_ok=True)
## Iterate through each sheet and export to CSV
for sheet_name in xls.sheet_names:
    df = pd.read_excel(f'{wd}02_SoIB_2023_main.xlsx', sheet_name) # Read the sheet into a DataFrame
    df.to_csv(f'{wd}state_wise\\{sheet_name}.csv', index=False) # Export the DataFrame to CSV
    print(f'Sheet {sheet_name} exported to {sheet_name}.csv')

## Remove non-state files
os.remove(f'{wd}state_wise\\README.csv')
os.remove(f'{wd}state_wise\\India.csv')
os.remove(f'{wd}state_wise\\Woodland.csv')
os.remove(f'{wd}state_wise\\Cropland.csv')
os.remove(f'{wd}state_wise\\ONEs.csv')
os.remove(f'{wd}state_wise\\PAs.csv')


# 2.  Select only relevant columns from all state csv files and add a new column for state name in each.
## Get a list of all files in the state_wise folder
state_csvs = os.listdir(f'{wd}state_wise')
## Define a list of columns to keep
col_keep = ['English Name', 'Scientific Name', 'SoIB 2023 Priority Status', 'Order',
            'Family', 'Endemicity', 'Habitat Specialization', 'IUCN Category','CITES Appendix']

## Create subfolder to store state csv files
os.makedirs(f'{wd}state_trim\\', exist_ok=True)
## Loop through each CSV file
for csv_file in state_csvs:
    ### Read the CSV file
    df1 = pd.read_csv(f'{wd}state_wise\\{csv_file}')
    df2 = df1[col_keep]
    ## Add new column with state names
    state = csv_file.split(sep='.')[0]
    df2['source'] = state
    ## Save to csv file
    df2.to_csv(f'{wd}state_trim\\{state}_trim', index=False)
    
    print(f'{csv_file} trimmed')


# 3. Combine all csvs into a single csv

## Initialize an empty DataFrame for visualization
data_vis = pd.DataFrame()

## Get a list of all CSV files in the state_trim folder
state_csvs = os.listdir(f'{wd}state_trim')

## Loop through each CSV file
for csv_file in state_csvs:
    ### Read the CSV file
    df1 = pd.read_csv(f'{wd}state_trim\\{csv_file}')
    ### Append the DataFrame to data_vis
    data_vis = pd.concat([ data_vis, df1], axis= 0 )

## Save to csv
data_vis.to_csv(f'{wd}all_birds.csv')
### To check, print the number of states 
print(set(data_vis['source']))
import pandas as pd
import os

# 1.  Select only relevant columns from all state csv files and add a new column for state name in each.
### Set the working directory
working_directory = 'F:\\Python_projects\\state_of_birds_india\\states\\'  
trim_directory = 'F:\\Python_projects\\state_of_birds_india\\trim\\'

### Get a list of all files in the working directory
all_files = os.listdir(working_directory)

### Filter only CSV files
csv_files = [file for file in all_files if file.endswith(".csv")]

### Loop through each CSV file
for csv_file in csv_files:
    #### Construct the full file path
    csv_path = working_directory + csv_file
    #### Read the CSV file
    ct_raw = pd.read_csv(csv_path)

    #### Keep only required columns
    ct = ct_raw.iloc[:, [0, 1, 2, 9, 10, 14, 18, 21, 23]]
    
    ### Keep one column with state names
    #### Extract state from file name
    state = csv_file.split(sep='.')[0]
    #### Extract state name without _
    state_name = ' '.join(state.split(sep='_'))
    #### New column with state name
    ct['source'] = state_name
    
    #### Save the trimmed DataFrame as a new CSV file in the 'trim' directory
    trim_path = trim_directory + csv_file
    #### Convert to csv and save
    ct.to_csv(trim_path, index=False)


# 2. Prepare a single csv for analysis and visualization

## 2.1 Combine Jammu_and_Kashmir.csv and Ladakh.csv into one csv
### Read both files
dir1 = trim_directory + 'Jammu_and_Kashmir.csv'
df1 = pd.read_csv(dir1)
dir2 = trim_directory + 'Ladakh.csv'
df2 = pd.read_csv(dir2)

### Combine into one and rename source column
df3 = pd.concat([df1, df2], ignore_index=True)
df3['source'] = 'Jammu and Kashmir'

### Save as Jammu_and_Kashmir.csv and remove Ladakh.csv
df3.to_csv(dir1, index=False)
os.remove(dir2)

## 2.2 Combine all csvs into a single csv

### Initialize an empty DataFrame for visualization
data_vis = pd.DataFrame()

### Get a list of all CSV files in the trim directory
csv_files = [file for file in os.listdir(trim_directory) if file.endswith('.csv')]

### Loop through each CSV file
for csv_file in csv_files:
    #set working directory
    dir = working_directory + csv_file
    #read csv
    df = pd.read_csv(dir)

    #Append the DataFrame to data_vis
    data_vis = pd.concat([ data_vis, df], axis= 0 )

### Save to csv
data_vis.to_csv('F:\\Python_projects\\state_of_birds_india\\birds_vis\\all_birds.csv')
### To check, print the number of states 
len(set(data_vis['source']))
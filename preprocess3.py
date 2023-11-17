import pandas as pd
import plotly.express as px
import geopandas as gpd

# Consistent state names across India Admin 1 geopackage and all_birds.csv

### Read both files
all_birds = pd.read_csv('F:\\Python_projects\\state_of_birds_india\\birds_vis\\all_birds.csv')
ind_adm1_raw = gpd.read_file('F:\\Python_projects\\state_of_birds_india\\birds_vis\\IND_adm1.gpkg')

### Check differences in state names in both dataframes
elements_only_in_ind_adm1 = sorted(set(ind_adm1_raw['NAME_1']).difference(set(all_birds['source'])))
elements_only_in_all_birds = sorted(set(all_birds['source']).difference(set(ind_adm1_raw['NAME_1'])))

print("Elements only in ind_adm1 (in alphabetical order):", elements_only_in_ind_adm1)
print("Elements only in all_birds (in alphabetical order):", elements_only_in_all_birds)

### Replace ind_adm1 state names with one in all_birds.csv
ind_adm1_raw['NAME_1'].iloc[0] ='Andaman and Nicobar Islands'
ind_adm1_raw['NAME_1'].iloc[25] ='Odisha'
ind_adm1_raw['NAME_1'].iloc[34] ='Uttarakhand'

### Only keep relevant columns
ind_adm1_raw = ind_adm1_raw[['ID_1', 'NAME_1', 'ENGTYPE_1', 'geometry']]

### Save as a new gpkg
ind_adm1_raw.to_file('F:\\Python_projects\\state_of_birds_india\\birds_vis\\IND_adm1.gpkg', driver='GPKG')
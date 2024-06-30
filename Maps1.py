import pandas as pd
import plotly.express as px
import geopandas as gpd
import matplotlib.pyplot as plt
import kaleido
import plotly.io as pio
import mapclassify


wd = 'F:\\github\\birds_vis\\'

# Read SoIB csv file
all_birds = pd.read_csv(f'{wd}all_birds.csv')
# Load shapefile of India with states polygons
ind_states = gpd.read_file(f'{wd}IND_state.gpkg')
india = ind_states.to_crs(epsg='24378') # Convert to appropriate CRS

# 1. Bar graph of birds in each state
state_wise = all_birds.groupby('source').count().reset_index()[['source', 'Unnamed: 0']]
state_wise.rename(columns={'Unnamed: 0': 'No of species'}, inplace=True)
result = pd.merge(india, state_wise, how='left', left_on='STATE', right_on='source')

state_wise_count = px.bar(result.sort_values(by='No of species', ascending =True),  x ='No of species', y= 'source',
                title= 'State-wise bird count',
                color = 'No of species' , color_continuous_scale=['red','black'], text='No of species')
## Axis titles
state_wise_count.update_layout(xaxis_title="Species count", yaxis_title='State',
                       font = dict(size=12))
## Remove colorbar
state_wise_count.update_coloraxes(showscale=False)
## Set the height of the figure to scale
state_wise_count.update_layout(height=1500)
## Save bar graph as image
pio.write_image(state_wise_count, 'state_wise_count_bargraph.png', engine="kaleido")


# 2. Map of no.of birds in each state
## Plot with color bar
fig, ax = plt.subplots(1, 1, figsize=(10, 10))

## Use a single color bar for the entire plot
cax = plt.cm.ScalarMappable(cmap='viridis_r')
cax.set_array(result['No of species'])

result.plot(column='No of species', 
            scheme='quantiles', k=5, cmap='viridis_r', 
            edgecolor='black', linewidth=0.25, 
            ax=ax, cax=cax)

ax.set_title('Different types of birds in each state as per the State of Indian Birds report 2023')
ax.set_axis_off()
ax.autoscale()

## Set the color bar label
cax.set_clim(result['No of species'].min(), result['No of species'].max())
cbar = fig.colorbar(cax, ax=ax, format = '%0.0f')
cbar.set_label('No. of different bird species')

## Save the plot as an image
plt.savefig('state_wise_count.png', bbox_inches='tight', dpi=300)
print('Prepared map for a state wise count of all birds')


# 3. Define a function to create relevant maps and display a list of species as per our criteria

def stat_tab(df, iucn, soib):
        # Filter by criteria
        iucn_soib = df[(df['IUCN Category'] == iucn) & (df['SoIB 2023 Priority Status'] == soib)]
        
        # Print a list of species
        #print(iucn_soib['English Name'].unique())
        
        # Dtaframe grouped by state and counts of birds
        state_wise = iucn_soib.groupby('source').count().reset_index()[['source', 'Unnamed: 0']]
        # Left join with India states shapefile
        result = pd.merge(india, state_wise, how='left', left_on='STATE', right_on='source')
        # Replace NA values with 0 in the count column
        result['Unnamed: 0'].fillna(0, inplace=True)
        # Round up numbers to 0 decimal places
        result['Unnamed: 0'] = round(result['Unnamed: 0'], 0)
        #print(result)
        
        # Plot with color bar
        fig, axes = plt.subplots(1, 2, figsize=(20, 10))
        
        # Use a single color bar for the entire plot
        cax = plt.cm.ScalarMappable(cmap='viridis_r')
        cax.set_array([result['Unnamed: 0']])
        
        ax=axes[0]
        n=len(result['Unnamed: 0'].unique())-2        
        result.plot(column='Unnamed: 0', scheme='quantiles', k=n, cmap='viridis_r', edgecolor='yellow', linewidth=0.25, 
                ax=ax, cax=cax)
        
        ax.set_title(f'Species richness map of India for {iucn} and {soib} priority birds')
        ax.set_axis_off()
        ax.autoscale()
        
        ax2=axes[1]
        # Display the list vertically
        for i, text in enumerate(iucn_soib['English Name'].unique()):
                ax2.text(0.1, 0.95 - 0.03 * i, text, ha='left', va='center', transform=ax2.transAxes)
        ax2.set_title(f'List of Birds with \n IUCN status: {iucn} \n SOIB23 status: {soib}', loc='left')
        ax2.set_axis_off()
        ax2.autoscale()
        
        # Set the color bar label
        cax.set_clim(result['Unnamed: 0'].min(), result['Unnamed: 0'].max())
        cbar = fig.colorbar(cax, ax=ax, format = '%0.0f',pad=0.01, location = 'left')
        cbar.set_label('No. of different bird species')
        
        # Adjust the layout to prevent overlap
        plt.tight_layout()
        
        #Adjust position of both plots
        ax.set_position([0.1, 0.1, 1, 0.8]) 
        ax2.set_position([0.5, 0.1, 0.1, 0.6])
        
        # Save figure as png
        plt.savefig(f'F:\\github\\birds_vis\\fig_{iucn}_{soib}.png', bbox_inches='tight', dpi=300)
  
        # Display success message
        print(f'Prepared map for {iucn} and {soib} priority birds')
        
        
stat_tab(df = all_birds, iucn = 'Critically Endangered', soib = 'High')
stat_tab(df = all_birds, iucn = 'Endangered', soib = 'High')

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

state_wise = all_birds.groupby('source').count().reset_index()[['source', 'Unnamed: 0']]
state_wise.rename(columns={'Unnamed: 0': 'No of species'}, inplace=True)
result = pd.merge(india, state_wise, how='left', left_on='STATE', right_on='source')

state_wise_count = px.bar(result.sort_values(by='No of species', ascending =True),  x ='No of species', y= 'source',
                title= 'State-wise bird count',
                color = 'No of species' , color_continuous_scale=['red','black'], text='No of species')
#Axis titles
state_wise_count.update_layout(xaxis_title="Species count", yaxis_title='State',
                       font = dict(size=12))
#Remove colorbar
state_wise_count.update_coloraxes(showscale=False)
# Set the height of the figure to scale
state_wise_count.update_layout(height=1500)
## Save bar graph as image
pio.write_image(state_wise_count, 'state_wise_count.png', engine="kaleido")


result['No of species'] = round(result['No of species'], 0)
ax = result.plot(column = 'No of species', 
                scheme= 'quantiles', k=5, cmap='viridis_r', 
                legend = True, 
                edgecolor='white', linewidth=0.25)
ax.set_title('State wise bird count')
ax.set_axis_off()
ax.autoscale()
## Save bar graph as image
pio.write_image(state_wise_count, 'state_wise_count.png', engine="kaleido")

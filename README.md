# Which state to prioritize for bird conservation in India?
This is a mini-project I did to get better at data visualization using plotly to display maps in Python.

## Aim: 
To find which Indian states hold the most number of critically endangered and endangered species. This may help prioritize state-level bird conservation. 
 
## Data source: 
The Complete Table of Species Conservation Assessments data associated with the State of India’s Birds 2023 (SOIB23) report.
I also used a shapefile of Indian states obtained from the Survey of India website which I tweaked a bit in QGIS to adjust the state names as per the Assessment data. 

## Analysis: 
Using the raw data, I created a CSV file (all_birds.csv) containing bird species with corresponding IUCN and SOIB status and the name of the state it is found in. 
I then left joined all_birds.csv with the shapefile of Indian states (IND_state.gpkg) and made a map using plotly.
Finally, I produced two maps for birds classified as SOIB- 'High' priority and IUCN classification 'Critically Endangered' and 'Endangered'.
The colour of states corresponds to the no.of selected status bird species found in the state.

## Result: 
My initial analysis corresponds with Table 5 from the SOIB23 identifying species within IUCN classification and SOIB conservation priorities. 
### Table 1: Correspondence between IUCN Red List Categories and SoIB Categories of Conservation Priority (Source: State of India’s Bords 2023 - Table 5)
SoIB23 conservation priority, IUCN classification, Count
High, Critically Endangered, 14
Low, Critically Endangered, 1
Moderate, Endangered, 15

### Critically endangered and high priority: 
A species richness map (Figure 1) shows Rajasthan, Maharashtra, Assam and Arunachal Pradesh with high numbers of critically endangered species. 
### Endangered and high priority: 
A species richness map (Figure 2) shows Rajasthan, and West Bengal with high numbers of endangered species. 
The north-western state of Rajasthan is home to 7 critically endangered and 8 endangered species of high priority. This includes 6 species of the family Accipitridae (Hawks, Eagles, and Kites). High-priority species also prefer a wide variety of habitats with most found in wetlands or open habitats. 

## Conclusions: 
I suggest conservation be prioritized in Rajasthan, especially for Hawkes, Eagles and Kites for maximum impact of conservation efforts. 
In the case of conservation by way of habitat restoration and creation, wetland and Open habitat types can be selected since they each support up to 4 different species of high-priority birds. 

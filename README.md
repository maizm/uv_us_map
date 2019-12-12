
# Ultraviolet radiation :sunny: in the United States :us:
  **Mapping environmental or lifestyle factors based on the county FIPS codes**
      (Any factors with FIPS codes can be mapped using this python project, in addition to ultraviolet radiation)

## Introduction
To map the distribution of ultravioletra radiation (UVR) in the United States UVR.
   
## Modules and functions
  (require 'pandas', 'urllib.request', 'json',  'plotly.graph_objects')
  
### I. load_uvb_data.py: to download and load your own data as csv file, in my example it is UVR data
**1. Download the testing date** from https://github.com/maizm/uv_us_map/blob/master/data/July_15_2015.csv or using your own data with FIPS code
**2. Save the date onto your local computer**, e.g. "C:\Users\maiz2\Desktop\Python\uv\July_15_2015.csv"
**3. Load the date onto the Python**
   from pandas import read_csv  #require 'read_csv' from 'pandas'
   uv = read_csv(r'C:\Users\maiz2\Desktop\Python\uv\July_15_2015.csv') # 'r' indicate to load from your local address. You should change the following in your own local address
**4. before mapping, show the range of ultraviolet radiation B**
   minimum = uv['i305'].min()
     print("minimum uvb: " + str(minimum))  #minimum uvb#
   maximum = uv['i305'].max()
     print("maximum uvb: " + str(maximum))  #maximum uvb#
     
### III. map_US_uv.py: to map your own data in the United States

## Testing
Coming soon...

## Dependencies
1. Pandas
2. Urllib.request
3. json
4. plotly.graph_objects


### References
Plotly Technologies Inc. Title: Collaborative data science Publisher: Plotly Technologies Inc. Place of publication: Montréal, QC Date of publication: 2015 URL: https://plot.ly/python/reference/#choropleth

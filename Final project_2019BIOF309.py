# 1. Download the testing date from https://github.com/maizm/uv_us_map/blob/master/data/July_15_2015.csv or using your own data with FIPS code
# 2. Save the date onto your local computer, e.g. "C:\Users\maiz2\Desktop\Python\uv\July_15_2015.csv"
# 3. Load the date onto the Python
from pandas import read_csv  #require 'read_csv' from 'pandas'
uv = read_csv(r'C:\Users\maiz2\Desktop\Python\uv\July_15_2015.csv') # 'r' indicate to load from your local address. You should change the following in your own local address

# 4. before mapping, show the range of ultraviolet radiation B#
minimum = uv['i305'].min()
print("minimum uvb: " + str(minimum))  #minimum uvb#
maximum = uv['i305'].max()
print("maximum uvb: " + str(maximum))  #maximum uvb#


from urllib.request import urlopen  #require 'urlopen' from 'urllib.request'
import json #require 'json'
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response) #above two rows were used to load United States' map by each county

import pandas as pd #require 'pandas'
df = pd.read_csv(r"C:\Users\maiz2\Desktop\Python\uv\July 15 2015.csv", dtype={"countyfips": str})  # read csv file in my own local address, classfy the 'countyfips' as a string variable

import plotly.graph_objects as plt #require 'plotly.graph_objects'

fig = plt.Figure(plt.Choroplethmapbox(geojson=counties, locations=df.countyfips, z=df.i305, # 'counties' as the unit, countyfips to define the location, and ultraviolet radiation data: i305
                                    colorscale="Viridis", zmin=0, zmax=100,   #adjust ‘zmin’ and ‘zmax’ based on the minimum and maximum values in that specific date#
                                    marker_opacity=0.5, marker_line_width=0)) # personalization the figure
fig.update_layout(mapbox_style="carto-positron", # raster and vectior basemaps
                  mapbox_zoom=3, mapbox_center = {"lat": 37.0902, "lon": -95.7129}) # the displaying center point, you can adjust as your own.
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
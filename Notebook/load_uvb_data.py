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
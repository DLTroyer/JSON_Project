import json

#This is the first file we need to open 9/1-9/13
in_file = open('US_fires_9_14.json','r')

#define the fire_data list object
fire_data = json.load(in_file)

#initialize the variable lists
bness, lons, lats, hover_texts = [],[],[],[]

for fire in fire_data:
    if fire['brightness'] > 450:
        brightness = fire['brightness']
        lon = fire['longitude']
        lat = fire['latitude']
        bness.append(brightness)
        lons.append(lon)
        lats.append(lat)
    else:
        continue

#graph the data across the US
from plotly.graph_objs import scattergeo, Layout
from plotly import offline

data = [{
    'type':'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [0.045* brightness for brightness in bness],
        'color':bness,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Brightness'}
    },

}]

my_layout = Layout(title='US Fires - 9/14/2020 through 9/20/2020')

fig = {'data': data, 'layout':my_layout}

offline.plot(fig, filename='US_Fires_914_920.html')

import folium
import pandas as pd

data = pd.read_csv("testt.csv")
lat = list(data["point_latitude"])
lon = list(data["point_longitude"])
map = folium.Map(location=[29, -50.9], zoom_start=2, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My map")
i = 0
for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt, ln], popup="This is mark" + str(i), icon=folium.Icon(color="green")))
    i = i + 1
map.add_child(fg)
map.save("Map1.html")

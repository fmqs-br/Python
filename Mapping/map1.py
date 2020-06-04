import folium
import pandas

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")
data = pandas.read_csv("volcanoes.csv")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[38.58, -99.09], popup="Hi, I am a marker", icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("Map1.html")
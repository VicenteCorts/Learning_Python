# Primera web app Python
# Clase 127
# Trabajaremos con la librería Folium
## La aplicación recogerá tres capas, una priemra de mapa, una segunda que refleje la población y una tercera que muestre los volcanes por zonas.

# Clase 128-130
# pip3.13 install folium
import folium
# Sevilla:
map = folium.Map(location=[37.38283, -5.97317], zoom_start=15, tiles="OpenTopoMap")

fg = folium.FeatureGroup(name="My Map")

i = 1
for coordinates in [[37.38, -5.97],[37.387, -5.977],[37.385, -5.975]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Markador {}".format(i), icon=folium.Icon(color='green')))
    i = i+1

map.add_child(fg)

map.save("Map1.html")















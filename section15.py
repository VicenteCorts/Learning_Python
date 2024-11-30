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
fg.add_child(folium.Marker(location=[37.38, -5.97], popup="Markador 1", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")















# Primera web app Python
# Clase 127
# Trabajaremos con la librería Folium
## La aplicación recogerá tres capas, una priemra de mapa, una segunda que refleje la población y una tercera que muestre los volcanes por zonas.

# Clase 128-130
'''
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
'''

# Clase 131
'''
>>>import pandas
>>>data = pandas.read_csv("downloads/Calles_Sevilla.csv")
>>>data
# Todo OK
'''
# Librerías Importadas
import pandas
import folium

# Acceder al archivo y extraer las LAT y LON
data = pandas.read_csv("downloads/Calles_Sevilla.csv")
lat = list(data["LAT"])
lon = list(data["LON"])
nom = list(data["NOMBRE"])

# Variable html para insertar en el popup
html = """<h4>Nombre del marcador:</h4>
dirección: %s
"""

# Calase 135 Función para determinar el color en función de si es calle avda u otro
def determinar_color(calle):
    calle = calle.lower()
    color_variador = {
        'calle': 'blue',
        'avenida': 'red', 
        'plaza': 'green',
        'paseo': 'purple',
        'camino': 'orange',
        'boulevard': 'pink'
    }
    for tipo, color in color_variador.items():
        if tipo in calle:
            return color
    return 'gray'

# Crear mapa
map = folium.Map(location=[37.38283, -5.97317], zoom_start=15, tiles="OpenTopoMap")

# Crear Marcadores FeatureGroup
fg = folium.FeatureGroup(name="My Map")

# Bucle para recorrer las listas de LAT y LON (itera dos listas de manera simultánea)
for lt, ln, n in zip(lat, lon, nom):
    iframe = folium.IFrame(html=html % str(n), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color=determinar_color(n))))

# Afianzar Marcadores
map.add_child(fg)

# Crear archivo de mapa web
map.save("Map1.html")













# Clase 163
# Jupiter Notebook -> Graphs.ipynb
# (...)
# Clase 175
# Script para plottear los datos del script de la captura de movimiento:
'''
from section18 import df
from bokeh.plotting import figure, show, output_file

p=figure(x_axis_type='datetime', height=300, width=500, sizing_mode="stretch_width", title="Motion Graph")
# Estilos para el gráfico
p.yaxis.minor_tick_line_color=None
p.yaxis.ticker.desired_num_ticks=1

q=p.quad(left=df["Start"], right=df["End"], bottom=0, top=1, color="green")

output_file("Graph.html")

show(p)
# Para correr el programa escribimos en la consola python section19.py o le damos a correr
'''

# Clase 176 -> Añadiendo hover con info a los bloques de movimeinto del gráfico
from section18 import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

# Pasando a String los datetimes para poder trabajar con ellos
df["Start_string"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

# Método ColumnDatraSource para poder acceder a los datos en las figuras (hover)
cds=ColumnDataSource(df)

p=figure(x_axis_type='datetime', height=300, width=500, sizing_mode="stretch_width", title="Motion Graph")
# Estilos para el gráfico
p.yaxis.minor_tick_line_color=None
p.yaxis.ticker.desired_num_ticks=1

# Añadiendo Hover
hover=HoverTool(tooltips=[("Start", "@Start_string"), ("End", "@End_string")])
p.add_tools(hover)

q=p.quad(left="Start", right="End", bottom=0, top=1, color="green", source=cds)

output_file("Graph.html")

show(p)
# Clase 163
# Jupiter Notebook -> Graphs.ipynb
# (...)
# Clase 175
# Script para plottear los datos del script de la captura de movimiento:
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
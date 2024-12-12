import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

data = pandas.read_csv("downloads/reviews.csv", parse_dates=['Timestamp'])
data['Day'] = data['Timestamp'].dt.date
day_average = data.groupby(['Day']).mean(numeric_only=True)

chart_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: ''
    },
    subtitle: {
        text: ''
    },
    xAxis: {
        
        reversed: false,
        title: {
            enabled: true,
            text: 'Date'
        },
        labels: {
            format: '{value}'
        },
        
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        },
        labels: {
            format: '{value}'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: 'day: {point.x} || {point.y} Av. Rating'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Rating',
        data: []
    }]
}
"""

def app():
    wp = jp.QuasarPage()

    h1 = jp.QDiv(a=wp, text="Análisis de las Valoraciones de los Cursos", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="Estos Gráficos representan un análisis de las Valoraciones de los Cursos", classes="text-h6 text-center q-pa-md")
    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.title.text="Media de Valoraciones por Día"

    hc.options.xAxis.categories = list(day_average.index)
    hc.options.series[0].data = list(day_average['Rating'])

    return wp

jp.justpy(app)
import justpy as jp
import pandas
from datetime import datetime
from pytz import utc

data = pandas.read_csv("downloads/reviews.csv", parse_dates=['Timestamp'])
data['Week'] = data['Timestamp'].dt.strftime('%Y-%U') # String from time (strftime)
week_average=data.groupby(['Week']).mean(numeric_only=True)

chart_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Atmosphere Temperature by Altitude'
    },
    subtitle: {
        text: 'According to the Standard Atmosphere Model'
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
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Rating'
        },
        labels: {
            format: '{value}°'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
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
        name: 'Media de Valoraciones por Semana',
        data: [
            [0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]
        ]

    }]
}
"""

def app():
    wp = jp.QuasarPage()

    h1 = jp.QDiv(a=wp, text="Análisis de las Valoraciones de los Cursos", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="Estos Gráficos representan un análisis de las Valoraciones de los Cursos", classes="text-h6 text-center q-pa-md")
    
    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.title.text="Media de Valoraciones por Semana"

    hc.options.xAxis.categories = list(week_average.index)
    hc.options.series[0].data = list(week_average['Rating'])


    return wp

jp.justpy(app)
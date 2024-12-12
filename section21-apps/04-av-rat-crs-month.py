import justpy as jp
import pandas
from datetime import datetime
from pytz import utc

data = pandas.read_csv("downloads/reviews.csv", parse_dates=['Timestamp'])
data['Month'] = data['Timestamp'].dt.strftime("%Y-%m")
month_av_crs = data.groupby(['Month','Course Name']).mean(numeric_only=True).unstack()

chart_def = """
{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Average Rating by Course through the Months'
    },
    subtitle: {
        text: ''
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 65,
        y: 180,
        floating: false,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF'
    },
    xAxis: {
         type: "category",
        dateTimeLabelFormats: {
            month: '%Y-%m'
        },
        title: {
            text: 'Date'
        },
        labels: {
            format: '{value}'
        }
    },
    yAxis: {
        title: {
            text: 'Rating'
        }
    },
    tooltip: {
        shared: true,
        headerFormat: '<b>Average Rating {point.x}</b><br>'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        series: {
            pointStart: 2000
        },
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: '',
        data:
            []
    }, {
        name: '',
        data:
            []
    }]
}
"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis", classes="text-h6 text-center q-pa-md")
    
    hc = jp.HighCharts(a=wp, options=chart_def)

    hc.options.xAxis.categories = list(month_av_crs.index)
    hc_data = [{"name": v1, "data":[v2 for v2 in month_av_crs[v1]]} for v1 in month_av_crs.columns]
    hc.options.series = hc_data
 
    return wp
 
jp.justpy(app)
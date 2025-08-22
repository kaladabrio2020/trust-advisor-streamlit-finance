import pandas as pd 
import plotly.graph_objects as go


def plot_pie_type(data):
    subset = data.groupby(['Type'])[['Value']].agg(['count', 'sum']).reset_index()
    subset.columns = ['Type', 'count', 'sum']
    fig = go.Figure([
        go.Pie(
            labels = subset['Type'].tolist(),
            values = subset['count'].tolist(),
            customdata=subset['sum'].apply(lambda x: round(x, 2)).tolist(),
        )
    ])
    
    fig.update_traces(
        textinfo = 'percent+value',
        marker   = dict(
            colors = ['#e63946', '#457b9d', '#dda15e'],
        ),
        hoverlabel = dict(
            bgcolor = '#f8f9fa',
        ),
        hovertemplate = 'Type : %{label} <br>Quantity : %{value} <br>Percentage : %{percent}<br>Total : %{customdata}<extra></extra>'
    )

    fig.update_layout(
        title = dict(
            text = 'Type of Portfolium',
            font = dict(
                size = 18,
                weight = 'bold',
                color  = '#22333b'
            )
        ),
        legend = dict(
            title = dict(
                text = 'Type',
            ),
            font = dict(
                color  = '#22333b'
            )
        ),
        font = dict(
            family = 'inter, sans-serif',
        ),
        margin = dict(
            l = 50,
            b = 50,
        ),
        width = 500,
        height= 400,
        dragmode = None
    )
    return fig
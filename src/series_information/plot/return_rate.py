import numpy as np
import pandas as pd
import plotly.graph_objects as go


FONT_FAMILY = 'ui-sans-serif,-apple-system,system-ui,Segoe UI,Helvetica,Apple Color Emoji,Arial,sans-serif,Segoe UI Emoji,Segoe UI Symbol'

def plot_return_rate(data, window=0):

    if window == 0:
        data['return_rate'] = data['Close'] - data['Open']
    else:
        data['return_rate'] = data['Close'].pct_change(window)
        data = data.dropna()

    fig = go.Figure([
        go.Scatter(
            x=data.index, 
            y=data['return_rate'], 
            mode='lines'
        )
    ])

    fig.update_traces(
        hoverlabel = dict(
            bgcolor = 'white',
            font = dict(
                size = 16
            )
        ),
        hovertemplate = '%{x} <br> Return Rate : %{y}<extra></extra>'
    )
    
    title_text = 'Return Rate, the last '+ str(window) + ' days'

    fig.add_hline(
        y=0, 
        line_width=2,
        line_dash ='solid', 
        line_color="black"
    )
    fig.update_layout(
        title = dict(
            text = title_text,
            font = dict(
                family = FONT_FAMILY,
                weight = 'bold'
            ) 
        ),
        xaxis = dict(
            title = dict(
                text = 'Date'
            )
        ),
        yaxis = dict(
            title = dict(
                text = 'Return Rate'
            )
        ),
        
        font = dict(
            family = FONT_FAMILY,
        ),
        template = 'simple_white',
        hovermode = 'x'
    )
    return fig
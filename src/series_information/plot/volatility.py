import numpy as np
import pandas as pd
import plotly.graph_objects as go

FONT_FAMILY = 'ui-sans-serif,-apple-system,system-ui,Segoe UI,Helvetica,Apple Color Emoji,Arial,sans-serif,Segoe UI Emoji,Segoe UI Symbol'

def plot_volatility(data):
    # daily Volatility : Close - Open
    
    subset = data['Close'].pct_change().resample('ME').std() * np.sqrt(252)
    
    fig = go.Figure([
        go.Scatter(
            x=subset.index, 
            y=subset.values.flatten(), 
            mode='lines',
            customdata=subset.index.strftime('%Y-%m-%d')
        )
    ])

    title_text = 'Monthly Volatility'

    fig.update_traces(
        hovertemplate = '%{customdata} <br> Volatility : %{y}<extra></extra>'
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
                text = 'Volatility'
            )
        ),
        font = dict(
            family = FONT_FAMILY,
        ),
        template = 'simple_white',
        height = 350
    )
    return fig
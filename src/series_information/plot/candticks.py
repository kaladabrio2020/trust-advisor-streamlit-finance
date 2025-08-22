import numpy as np
import pandas as pd
import plotly.graph_objects as go

FONT_FAMILY = 'ui-sans-serif,-apple-system,system-ui,Segoe UI,Helvetica,Apple Color Emoji,Arial,sans-serif,Segoe UI Emoji,Segoe UI Symbol'

def plot_chat_candlestick(data, symbol='BTC-USD', scale=None):
    if scale == 'log':
        data = data.apply(lambda x: np.log1p(x))
        
    elif scale == 'sqrt':
        data = data.apply(lambda x: np.sqrt(x))

    
    fig = go.Figure([
        go.Candlestick(
            x=data.index,
            open=data['Open'].values.flatten(),   # transforma em 1D
            high=data['High'].values.flatten(),
            low=data['Low'].values.flatten(),
            close=data['Close'].values.flatten(),
        )
    ])
    fig.update_traces(
        hoverlabel = dict(
            font = dict(
                size = 16
            )
        )
    )
    fig.update_layout(
        title = dict(
            text = f'Candlestick {symbol}',
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
        font = dict(
            family = FONT_FAMILY
        ),
        margin = dict(
            l = 10,
            r = 10,
            t = 40,
            b = 40
        ),
        template = 'simple_white',
        hovermode = 'x unified',
        xaxis_rangeslider_visible=False

    )
    return fig
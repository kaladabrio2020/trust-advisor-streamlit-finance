import plotly.graph_objects as go


def volatility(data):
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=data.index, y=data['volatility'], mode='lines'))

    fig.update_layout(
        title='Volatility',
        xaxis_title='Date',
        yaxis_title='Volatility',
    )
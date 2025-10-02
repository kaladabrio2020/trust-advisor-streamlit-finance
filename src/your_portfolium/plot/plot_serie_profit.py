import plotly.graph_objects as go


FONT_FAMILY = 'ui-sans-serif,-apple-system,system-ui,Segoe UI,Helvetica,Apple Color Emoji,Arial,sans-serif,Segoe UI Emoji,Segoe UI Symbol'

def plot_serie_profit(subs):
    fig = go.Figure([
        go.Scatter(
            x = subs.index,
            y = subs,
        )
    ])

    fig.update_traces(
        hovertemplate = 'Date : %{x} <br>Profit : %{y}<extra></extra>',
        marker = dict(
            color = '#2a9d8f'
        
        )
    )
    fig.update_layout(
        title = dict(
            text = 'Serie Profit',
            font = dict(
                size = 18,
                weight = 'bold',
                color  = '#22333b'
            )
        ),
        font = dict(
            family = FONT_FAMILY,
        ),
        margin = dict(
            l = 50,
            b = 50,
        ),
        height= 400,
        template = 'simple_white',
        dragmode=None
    )
    return fig
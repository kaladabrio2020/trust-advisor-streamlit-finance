import plotly.graph_objects as go

FONT_FAMILY = 'ui-sans-serif,-apple-system,system-ui,Segoe UI,Helvetica,Apple Color Emoji,Arial,sans-serif,Segoe UI Emoji,Segoe UI Symbol'

def plot_area_profit(subs):
    fig = go.Figure([
        go.Bar(
            x = subs.index,
            y = subs,
            customdata=subs.index.astype(str),
        )
    ])
    

    fig.update_traces(
        hovertemplate = 'Date : %{customdata} <br>Profit : %{y}<extra></extra>',
        marker = dict(
            color = [
                '#2a9d8f' if x > 0 else '#e63946' for x in subs
            ]
        )
    )
    fig.update_layout(
        title = dict(
            text = 'Serie Profit PTC',
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
        template = 'simple_white',
        hovermode='x unified',
        dragmode=None,
        height = 400

    )
    return fig
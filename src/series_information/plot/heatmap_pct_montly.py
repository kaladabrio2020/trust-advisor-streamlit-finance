import plotly.express as px 
import plotly.graph_objects as go

FONT_FAMILY = 'ui-sans-serif,-apple-system,system-ui,Segoe UI,Helvetica,Apple Color Emoji,Arial,sans-serif,Segoe UI Emoji,Segoe UI Symbol'

import plotly.express as px 
def plot_pct_change_data_monthly(subset):
    subset = subset.fillna('0')
    fig = go.Figure([
        go.Heatmap(
            z = subset.values, 
            x = subset.columns, 
            y = subset.index,
            text = subset.values,
            zmid=0,
            colorscale="RdYlGn",
            showscale=False,
        )
    ])
    fig.update_traces(
        texttemplate='%{text:.2f}%',
    )
    fig.update_layout(
        title = dict(
            text = 'Pct Change Data Monthly',
            font = dict(
                family = FONT_FAMILY,
                weight = 'bold'
            )
        ),
        font = dict(
            family = FONT_FAMILY,
            size = 14
        ),
        template = 'simple_white',
        dragmode=None,
        height=600,
        xaxis = dict(
            tickvals = subset.columns,
            ticktext = subset.columns
        )
    )
    return fig
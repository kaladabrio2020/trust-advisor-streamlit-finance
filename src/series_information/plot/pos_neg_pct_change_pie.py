import plotly.express as px 
import plotly.graph_objects as go

FONT_FAMILY = 'ui-sans-serif,-apple-system,system-ui,Segoe UI,Helvetica,Apple Color Emoji,Arial,sans-serif,Segoe UI Emoji,Segoe UI Symbol'

def plot_pie_pos_neg_pct_change(subset):
    fig = go.Figure([
        go.Pie(
            labels = subset['is_positive'], 
            values = subset['count'], 
            textinfo = 'label+value+percent'
        )
    ])
    fig.update_traces(
        marker = dict(
            colors = ['#2a9d8f', '#e63946']
        )
    )

    fig.update_layout(
        title = dict(
            text = 'Positive and Negative Pct Change Data',
            font = dict(
                family = FONT_FAMILY,
                weight = 'bold'
            )
        ),
        font = dict(
            family = FONT_FAMILY,
            size = 14
        ),
        margin = dict(
            l = 10,
            b = 10,  
            r = 50
        ),
        template = 'simple_white',
        dragmode=None,
        height=300,
    )
    return fig
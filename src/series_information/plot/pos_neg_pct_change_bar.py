import plotly.express as px 
import plotly.graph_objects as go

FONT_FAMILY = 'ui-sans-serif,-apple-system,system-ui,Segoe UI,Helvetica,Apple Color Emoji,Arial,sans-serif,Segoe UI Emoji,Segoe UI Symbol'


def plot_pos_neg_pct_change(subset):
    fig = go.Figure([])

    for is_pos in subset['is_positive'].unique():
        subset_pos = subset[subset['is_positive'] == is_pos]

        fig.add_trace(
            go.Bar(
                x = subset_pos['month_name'], 
                y = subset_pos['count'], 
                name = is_pos,
                text = subset_pos['count'],
                orientation='v',
                marker=dict(
                    color = '#2a9d8f' if is_pos == 'positive' else '#e63946'
                )
            )
        )

    fig.update_layout(
        title = dict(
            text = 'Positive and Negative Pct Change Data Monthly',
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
        height = 350
    )
    return fig
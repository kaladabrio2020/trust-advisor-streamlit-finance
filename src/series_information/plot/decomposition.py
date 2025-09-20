import pandas as pd
import statsmodels.api as sm
from plotly.subplots import make_subplots
from plotly import graph_objects as go

FONT_FAMILY = 'ui-sans-serif,-apple-system,system-ui,Segoe UI,Helvetica,Apple Color Emoji,Arial,sans-serif,Segoe UI Emoji,Segoe UI Symbol'



def decompose_time_series(data, model='additive', freq=None):
    # model = 'additive' or 'multiplicative'
    # freq = None (let statsmodels decide) or integer (number of periods in a season)
    
    result = sm.tsa.seasonal_decompose(data['Close'].values.ravel(), model=model, period=freq)
    
    fig = go.Figure()
    # Transformar em DataFrame
    df_decomp = pd.DataFrame({
        "observed": result.observed,
        "trend": result.trend,
        "seasonal": result.seasonal,
        "resid": result.resid
    }, index=data.index)

    # Criar subplots com Plotly
    fig = make_subplots(rows=4, cols=1, shared_xaxes=True,
                        subplot_titles=("Observed", "Trend", "Seasonal", "Residuals"))

    fig.add_trace(
        go.Scatter(
            x=df_decomp.index, 
            y=df_decomp["observed"], 
            name="Observed"
        ), row=1, col=1
    )
    fig.add_trace(
        go.Scatter(
            x=df_decomp.index, 
            y=df_decomp["trend"], 
            name="Trend"
        ), row=2, col=1
    )
    fig.add_trace(
        go.Scatter(
            x=df_decomp.index, 
            y=df_decomp["seasonal"], 
            name="Seasonal"
            ), row=3, col=1
        )
    
    fig.add_trace(
        go.Scatter(
            x=df_decomp.index, 
            y=df_decomp["resid"], 
            name="Residuals"
        ), row=4, col=1
    )

    fig.update_layout(height=900, width=1000, title_text="Time Series Decomposition (Plotly)")
    fig.update_layout(
        title = dict(
            text = 'Decomposition of the time series',
            font = dict(
                family = FONT_FAMILY,
                weight = 'bold'
            )
        ),
        font = dict(
            family = FONT_FAMILY
        ),
        template = 'simple_white',
        dragmode=None,
        height=700
    )
    return fig
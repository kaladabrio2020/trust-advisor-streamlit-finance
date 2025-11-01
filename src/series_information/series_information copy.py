import streamlit as st
import pandas as pd
import pathlib
import os

from src.series_information.plot.candticks  import plot_chat_candlestick
from src.series_information.plot.volatility import plot_volatility
from src.series_information.plot.return_rate import plot_return_rate
from src.series_information.plot.decomposition      import decompose_time_series

# 
from src.series_information.plot.heatmap_pct_montly     import plot_pct_change_data_monthly
from src.series_information.plot.pos_neg_pct_change_bar import plot_pos_neg_pct_change
from src.series_information.plot.pos_neg_pct_change_pie import plot_pie_pos_neg_pct_change



from src.functions.gets_data import get_data, get_data_fred
from src.functions.trat_pct_moth import pct_change_data_monthly
from src.functions.trat_pct_moth_pos_neg import return_pos_neg_pct_change
from src.functions.stationary import test_stationary


DATA_DIR = pathlib.Path(os.getcwd())



def get_data_symbol():
    try:
        data = pd.read_csv(DATA_DIR / 'data' / 'your_portfolium.csv')
        return data['Symbol'].unique().tolist()
    
    except Exception as e:
        st.error(e.args[0])




def series_information():
    st.title("Series Information")

    ## Side bar
    st.sidebar.header("Series Information")
    
    ## Dataframe
    symbol = st.sidebar.multiselect(
        label    = 'Symbol/Name',
        max_selections=1,
        accept_new_options=True,
        placeholder='SYMBOL: BTC-USD, ^GSPC, ^VIX..',
        options = get_data_symbol(),
        default = 'BTC-USD'
    )

    segment_date = st.sidebar.multiselect(
        label = 'Segment Date',
        options = ['5d', '1mo', '3mo', '1y', '2y', '3y', 'max'],
        default = '1y',
        max_selections = 1,
        accept_new_options = False,
    )

    window = st.sidebar.slider('Return Rate', 0, 30, 0)
    
    st.sidebar.subheader("Decomposition Settings")

    type_decomposition = st.sidebar.selectbox(
        label = 'Type of Decomposition',
        options = ['additive', 'multiplicative'],
        index = 0,
        help = 'Additive: y(t) = T(t) + S(t) + e(t) | Multiplicative: y(t) = T(t) * S(t) * e(t)'
    )

    freq = st.sidebar.number_input(
        label = 'Frequency (Seasonal Period)',
        min_value = 2,
        max_value = 365,
        value = 5,
        step = 1,
        help = 'Number of periods in a season. Ex: 5 for weekly seasonality in daily data'
    )
    # Get data 
    try:
        symbol_, segment_date_, window_ = (
            symbol[-1],
            segment_date[-1],
            window
        )
        
        if len(symbol) != 0 and len(segment_date) != 0:
            data = get_data(symbol_, segment_date_)
            graph_series_information(data, symbol_, segment_date_, window_, type_decomposition, freq)
        
    except Exception as e:
        st.error(str(e))

def graph_series_information(data, symbol, segment_date, window, type_decomposition, freq):


    # Candlestick Chart
    with st.container(border=True):
        fig1 = plot_chat_candlestick(data, symbol)
        st.plotly_chart(fig1, use_container_width=True)


    ## GRAPH 1 e 2 = Volatility and Return Rate
    col1, col2 = st.columns([0.50, 0.50], border=True)

    with col1:
        fig2 = plot_volatility(data)
        st.plotly_chart(fig2, use_container_width=True)

    with col2:
        fig3 = plot_return_rate(data, window=window)
        st.plotly_chart(fig3, use_container_width=True)
    

    # Decomposition Series and Pct Change cat by month (with pie and bar)
    col3, col4 = st.columns([0.60, 0.40])
    with col3:
        fig4 = decompose_time_series(data, type_decomposition, freq)

        with st.container(border=True):
            st.plotly_chart(fig4, use_container_width=True)
    
    with col4:
        try:
            subset    = return_pos_neg_pct_change(pct_change_data_monthly(data)[1])

            fig6 = plot_pos_neg_pct_change(subset)
            fig7 = plot_pie_pos_neg_pct_change(subset)

            with st.container(border=True):
                st.plotly_chart(fig6, use_container_width=True)

            with st.container(border=True):
                st.plotly_chart(fig7, use_container_width=True)

        except Exception as e:
            st.error(str(e))

    # Pct Change for each month
    with st.container(border=True):
        try:
            subset, _ = pct_change_data_monthly(data)
            fig5 = plot_pct_change_data_monthly(subset)
            st.plotly_chart(fig5, use_container_width=True)
        except Exception as e:
            st.error(str(e))

    st.write(test_stationary(data, lags=window))


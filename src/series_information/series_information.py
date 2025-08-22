import streamlit as st
import pandas as pd
import pathlib
import os

from src.series_information.plot.candticks import plot_chat_candlestick
from src.functions.gets_data import get_data


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
   
    
    # Get data 
    try:
        symbol_, segment_date_ = symbol[-1], segment_date[-1]
        
        if len(symbol) != 0 and len(segment_date) != 0:
            data = get_data(symbol_, segment_date_)
            graph_series_information(data, symbol_, segment_date_)
        
    except Exception as e:
        st.error(str(e))

def graph_series_information(data, symbol, segment_date):
    with st.container(border=True):

        fig1 = plot_chat_candlestick(data, symbol)
        st.plotly_chart(fig1, use_container_width=True)

    col1, col2 = st.columns([0.35, 0.65], border=True)
    with col1:
        fig2 = plot_chat_candlestick(data, symbol, scale='log')
        st.plotly_chart(fig2, use_container_width=True)
    with col2:
        fig3 = plot_chat_candlestick(data, symbol, scale='sqrt')
        st.plotly_chart(fig3, use_container_width=True)

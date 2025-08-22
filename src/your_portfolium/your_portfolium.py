import os 
import pathlib
import datetime
import investpy
import pandas as pd
import streamlit as st 
import pkg_resources
## Functions 
from src.functions.exist_stocks_crypto_index import verify_symbol
from src.functions.save_data                 import save_data

## Plots
from src.your_portfolium.plot.plot_pie_type import plot_pie_type


## options
OPTIONS = ['Crypto', 'Stocks', 'ETF']
STOCKS = investpy.stocks.get_stocks(country="united states")['symbol'].unique().tolist()
ETF    = investpy.etfs.get_etfs(country="united states")['symbol'].unique().tolist()

DATA_DIR = pathlib.Path(__file__).parent.parent.parent

def your_portfolium():
    st.set_page_config(layout="wide", page_title="Your Portfolium", page_icon="📊")

    st.title("Your Portfolium")

    ## Side bar 
    st.sidebar.header("Portfolium")


    ## Type
    type_portfolium = st.sidebar.selectbox( label = 'Type of Portfolium', options = OPTIONS,  index = 0)
    
    options_ = ['None']
    match type_portfolium:
        case 'Stocks':
            options_ = STOCKS
        case 'ETF':
            options_ = ETF
        


    code_portfolium = st.sidebar.multiselect(
        label    = 'Symbol/Name',
        max_selections=1,
        accept_new_options=True,
        placeholder='SYMBOL: BTC-USD, ^GSPC, ^VIX..',
        options = options_
    )
    code_portfolium = code_portfolium[0] if len(code_portfolium) > 0 else 'doopiwmdampodajsreouibnadsi9384024908230/**/'
    ## value
    value_ = st.sidebar.text_input( label = 'Value', placeholder = 'Value of your portfolium' )

    ## Date
    date_ = st.sidebar.date_input( label = 'Date USD', value = datetime.date.today() )
    ## Submit 
    buttom = st.sidebar.button( label = 'Submit' )
    if buttom:
        os.makedirs(DATA_DIR / 'data', exist_ok=True)
        
        try:
            # Verify data 
            if len(code_portfolium) < 1:                           raise ValueError('Code must be at least 2 characters')
            if not verification(type_portfolium, code_portfolium): raise ValueError('Code does not exist')
            
            # Save data on csv      
            save_data(DATA_DIR / 'data' / 'your_portfolium.csv', [date_, type_portfolium, code_portfolium.upper(), float(value_)])
            st.success('Data saved')

        except ValueError as e: st.error(e.args[0])
        except Exception  as e: st.error(e.args[0])
        

    tab1, tab2 = st.tabs(["Graph", "Data"])

    with tab1: graph()
    with tab2: get_data_tabs()

##
def verification(type_portfolium, code_portfolium):

    if type_portfolium == 'Stocks':
        return verify_symbol(code_portfolium)
    elif type_portfolium == 'ETF':
        return True
    
    return False

##
@st.fragment
def get_data_tabs():
    try:
        st.dataframe(pd.read_csv(DATA_DIR / 'data' / 'your_portfolium.csv'))

        id_remove = st.text_input('Remove data by id')
        try:
            if len(id_remove) > 6:
                df = pd.read_csv(DATA_DIR / 'data' / 'your_portfolium.csv')
                df = df[df['id'] != id_remove]
                df.to_csv(DATA_DIR / 'data' / 'your_portfolium.csv', index=False)


        except Exception as e:
            st.error(e.args[0])

    except Exception as e:
        st.error(e.args[0])

def graph():
    data = pd.read_csv(DATA_DIR / 'data' / 'your_portfolium.csv')

    left_column, right_column = st.columns([0.35, 0.65], border=True)
    left_column.plotly_chart(plot_pie_type(data), use_container_width=False)
    right_column.write('dasdasda')
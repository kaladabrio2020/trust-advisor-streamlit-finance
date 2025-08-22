import os 
import pathlib
import datetime
import investpy
import pandas as pd
import streamlit as st 

## Functions 
from src.functions.exist_stocks_crypto_index import verify_symbol
from src.functions.save_data                 import save_data


## options
OPTIONS = ['Crypto', 'Stocks', 'Bonds']
stocks_symbol = investpy.stocks.get_stocks(country="united states")['symbol'].unique().tolist()


# Index Stocks Symbols
STOCKS = stocks_symbol

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
        


    code_portfolium = st.sidebar.multiselect(
        label    = 'Code',
        max_selections=1,
        accept_new_options=True,
        placeholder='SYMBOL: BTC-USD, ^GSPC, ^VIX..',
        options = 
    )
    ## value
    value_ = st.sidebar.text_input( label = 'Value', placeholder = 'Value of your portfolium' )

    ## Date
    date_ = st.sidebar.date_input( label = 'Date USD', value = datetime.date.today() )


    ## Submit 
    buttom = st.sidebar.button( label = 'Submit' )

    if buttom:
        os.makedirs(data_dir, exist_ok=True)
        data_dir = pathlib.Path(__file__).parent.parent.parent
        
        try:
            # Verify data 
            if not value_.isnumeric():                     raise ValueError('Value must be a number')
            if len(code_portfolium) <= 1:                  raise ValueError('Code must be at least 2 characters')
            if not verify_symbol(code_portfolium.upper()): raise ValueError('Code does not exist')

            # Save data on csv      
            save_data(data_dir / 'data' / 'your_portfolium.csv', [date_, type_portfolium, code_portfolium.upper(), float(value_)])
            st.success('Data saved')

        except ValueError as e: st.error(e.args[0])
        
        except: st.error('Value must be a number')
        
        # If the directory does not exist, create it

import yfinance 
import investpy
import pandas as pd
import pathlib

BASE_DIR = pathlib.Path(__file__).parent.parent.parent

def get_data_yfinance(symbol: str, period: str) -> pd.DataFrame:
    try:
        data = yfinance.download(symbol, period=period, auto_adjust=True)
        if data.empty:
            raise Exception(f"Symbol {symbol} not found in yfinance")
        return data
    except Exception:
        return None  # fallback para tentar investpy

def get_data_investpy(symbol: str, period: str) -> pd.DataFrame:
    try:
        dados = investpy.stocks.get_stock_historical_data(symbol, country='united states', from_date='01/01/2000', to_date='31/12/2025')
        if dados.empty:
            return None
        return dados
    except Exception:
        return None

def get_data(symbol: str, period: str) -> pd.DataFrame:
    data = get_data_yfinance(symbol, period)
    
    if data is None:
        data = get_data_investpy(symbol, period)
    
    if data is None:
        raise Exception(f"Symbol {symbol} not found in any provider")
    
    return data


import requests
import pickle
def get_data_fred(symbol: str) -> pd.DataFrame:
    try:
        with open(BASE_DIR / 'config' / 'api_fred.pkl', 'rb') as f:
            api = pickle.load(f)

        response = requests.get(f'https://api.stlouisfed.org/fred/series/observations?series_id={symbol}&api_key={api}&file_type=json')
        data = yfinance.download(symbol, period="1d")
        return data
    except Exception as e:
        st.error(e.args[0])
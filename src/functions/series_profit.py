import pandas as pd 
import yfinance

# calcula o retorno percentual de um único ativo
# calcula o retorno percentual de um único ativo
def calculate_profit(series, data):
    initial_price = series['Close'].iloc[0, :][0]
    profit = ((series['Close'] - initial_price) / initial_price) * data['Value'][1]
    return round(profit, 3)

# soma os retornos de todos os ativos
def aggregate_profits(profit_list):
    total = pd.concat(profit_list, axis=1).fillna(0).sum(axis=1)
    total = total.reset_index(name='profit')
    # total['price'] = total['profit'] + data['Value'].sum()
    return round(total,3)

# pipeline principal para calcular os lucros de todos os símbolos
def compute_portfolio_profits(data):
    all_profits = []
    all_profits_pct = []
    for i in range(len(data['Symbol'])):
        series = yfinance.download(
            tickers=data['Symbol'][i],
            start=data['Date'][i],
            period='1y',
            interval='1d',
            auto_adjust=True
        )
        all_profits.append(calculate_profit(series, data))
    
    return aggregate_profits(all_profits).set_index('Date')


def serie_profit(data, subs):
    for i, row in data.iterrows():
        symbol = row['Symbol']
        date = pd.to_datetime(row['Date'])
        value = row['Value']

        if date not in subs.index:
            subs[date] = pd.Series(index=subs.columns, dtype=float)

        subs.at[date, symbol] = value
    subs = subs.ffill().fillna(0)

    return subs.sum(axis=1), subs

def serie_profit_pct(data, serie2):
    sum_ = serie2.drop(columns=['profit'])
    sum_ = sum_.sum(axis=1)

    return ((data - sum_) / sum_) * 100

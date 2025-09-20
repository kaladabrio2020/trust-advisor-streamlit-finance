import pandas as pd
month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def pct_change_data_monthly(data):
    series = data[['Close', 'Open']]
    series.columns = series.columns.droplevel(1)
    series = series.apply(lambda x: round(x, 2))
    
    # Resample para o último dia do mês
    closed = series['Close'].resample('ME').last()
    opened = series['Open'].resample('ME').first()
    
    # Calcular a taxa de retorno mensal
    series = ((closed - opened) / opened).reset_index(name='return_rate') 
    series = series.set_index('Date')

    # Porcentagem
    series = series.apply(lambda x: x*100)

    
    series['month_name'] = series.index.month_name()
    series['year']       = series.index.year

    # Ordenar 
    series['month_name'] = pd.Categorical(series['month_name'], categories=month_names, ordered=True)
    series = series.sort_values(by='month_name')
    # Agrupar por mês e ano
    return pd.pivot_table(series, values='return_rate', index='month_name', columns=['year']).apply(lambda x: round(x, 2)), series

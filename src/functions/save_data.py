import os 
import pandas as pd

def save_data(path, list_):           
    if os.path.exists(path):
        data_frame = pd.read_csv(path)
        data_frame.loc[len(data_frame)] = list_
        data_frame.to_csv(path, index=False)

    else:
        data_frame = pd.DataFrame(columns=['Date', 'Type', 'Symbol', 'Value'])
        data_frame.loc[len(data_frame)] = list_
        data_frame.to_csv(path, index=False)
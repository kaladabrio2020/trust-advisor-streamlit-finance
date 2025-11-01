import os 
import time 
import random 
import pandas as pd

def save_data(path, list_):    
     
    id = list_[1] + '_'+ time.strftime("%Y_%m_%d_%H_%M_%S") + '_' + str(random.randint(1, 1000))
    list_.insert(0, id)
    
    if os.path.exists(path):
        data_frame = pd.read_csv(path)
        data_frame.loc[len(data_frame)] = list_
        data_frame.to_csv(path, index=False)

    else:
        data_frame = pd.DataFrame(columns=['id', 'Date', 'Type', 'Symbol', 'Value'])
        data_frame.loc[len(data_frame)] = list_
        data_frame.to_csv(path, index=False)


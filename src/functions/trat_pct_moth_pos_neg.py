import pandas as pd
import numpy as np


def return_pos_neg_pct_change(series):
    series['is_positive'] = np.where(series['return_rate'] > 0, 1, 0)
    subset = series.groupby('month_name')['is_positive'].value_counts()
    subset = subset.reset_index()
    subset['is_positive'] = subset['is_positive'].apply(lambda x: 'positive' if x == 1 else 'negative')
    return subset
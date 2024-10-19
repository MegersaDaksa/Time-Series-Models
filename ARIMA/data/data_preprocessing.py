from statsmodels.tsa.stattools import adfuller
import pandas as pd

def preprocess_data(df):
    """ Data cleaning and stationarity checks """
    df['Close'] = df['Close'].fillna(method='ffill')
    result = adfuller(df['Close'])
    
    if result[1] > 0.05:
        df['Close_diff'] = df['Close'].diff().dropna()  # Differencing
    return df

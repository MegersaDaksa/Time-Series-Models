import yfinance as yf
import pandas as pd

def get_sp500_data():
    sp500 = yf.Ticker("^GSPC")
    df = sp500.history(period="max")
    
    return df[['Close']]
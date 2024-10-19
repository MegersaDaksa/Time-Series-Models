import yfinance as yf
import pandas as pd

def fetch_sp500_data():
    sp500 = yf.Ticker("^GSPC")
    data = sp500.history(period="max")
    return data[['Close']]

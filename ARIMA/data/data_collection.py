import yfinance as yf
import pandas as pd

def get_sp500_data(start_date, end_date):
    """ Fetch historical SP500 data from Yahoo Finance """
    sp500 = yf.download('^GSPC', start=start_date, end=end_date)
    return sp500

def fetch_sp500_data():
    sp500 = yf.Ticker("^GSPC")
    data = sp500.history(period="max")
    return data[['Close']]
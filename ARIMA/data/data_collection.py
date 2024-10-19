import yfinance as yf
import pandas as pd


def get_sp500_data(start_date, end_date):
    """ Fetch historical SP500 data from Yahoo Finance """
    sp500 = yf.download('^GSPC', start=start_date, end=end_date)
    return sp500

# Example usage
data = get_sp500_data('2010-01-01', '2024-01-01')
data.to_csv('../data/sp500.csv')  # Save to CSV

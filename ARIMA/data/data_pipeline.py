import yfinance as yf
import pandas as pd

def run_etl(start_date, end_date):
    data = get_sp500_data(start_date, end_date)
    cleaned_data = clean_data(data)
    cleaned_data.to_csv('processed_sp500_data.csv')
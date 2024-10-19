def run_etl():
    from ARIMA.data.data_collection import fetch_sp500_data
    from ARIMA.data.data_cleaning import clean_data
    
    data = fetch_sp500_data()
    cleaned_data = clean_data(data)
    cleaned_data.to_csv('processed_sp500_data.csv')
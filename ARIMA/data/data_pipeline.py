def run_etl():
    data = fetch_sp500_data()
    cleaned_data = clean_data(data)
    cleaned_data.to_csv('processed_sp500_data.csv')
def run_etl():
    data = fetch_sp500_data()
    clean_data = clean_data(data)
    clean_data.to_csv('processed_sp500_data.csv')  # Save for model input

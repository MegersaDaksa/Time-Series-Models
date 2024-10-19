# Databricks notebook source
# Import module
from ARIMA.data.data_collection import fetch_sp500_data
from ARIMA.data.data_cleaning import clean_data
from ARIMA.data.data_preprocessing import preprocess_data
from ARIMA.data.data_pipeline import run_etl

# ARIMA model building and prediction
from ARIMA.models.arima_model import build_arima_model

# Model training and evaluation
from ARIMA.models.model_training import train_arima_model
from ARIMA.models.model_evaluation import evaluate_model

# Model prediction
from ARIMA.models.model_prediction import predict_future_prices

import pandas as pd

# Data gathering
#data = fetch_sp500_data()
#data.to_csv('sp500_data.csv', index=False)

# Data preprocessing
train, test = preprocess_data(data.copy()) if isinstance(preprocess_data(data.copy()), tuple) else (preprocess_data(data.copy()), None)
# Ensure 'Close_diff' column exists in train DataFrame
if 'Close_diff' not in train.columns:
    train['Close_diff'] = train['Close'].diff()

# Build and train model
results = train_arima_model(train,1,1,1)

# Model evaluation
if test is not None:
    mse = evaluate_model(test['Close'], results['Predictions'])
    print(f"Model MSE: {mse}")
else:
    print("Test data is not available for evaluation.")

# Predict future prices
predictions = predict_future_prices(results, steps=30)
print(predictions)

# Run ETL pipeline
def run_etl():
    from ARIMA.data.data_collection import fetch_sp500_data
    from ARIMA.data.data_cleaning import clean_data
    
    data = fetch_sp500_data()
    cleaned_data = clean_data(data)
    cleaned_data.to_csv('processed_sp500_data.csv')

run_etl()

# COMMAND ----------

run_etl()

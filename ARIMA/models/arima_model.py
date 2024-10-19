from statsmodels.tsa.arima.model import ARIMA
import pandas as pd

def build_arima_model(data):
    model = ARIMA(data['Close'], order=(5, 1, 0))  # (p, d, q) values
    model_fit = model.fit()
    return model_fit
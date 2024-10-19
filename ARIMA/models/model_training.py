from statsmodels.tsa.arima.model import ARIMA
import pandas as pd
import pickle

def train_arima_model(data, p, d, q):
    """ Train ARIMA model with given parameters """
    model = ARIMA(data['Close_diff'].dropna(), order=(p, d, q))
    model_fit = model.fit()
    return model_fit

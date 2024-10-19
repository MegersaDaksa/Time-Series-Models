from sklearn.metrics import mean_squared_error

def evaluate_model(model_fit, test_data):
    predictions = model_fit.forecast(steps=len(test_data))
    rmse = mean_squared_error(test_data, predictions, squared=False)
    return rmse

import numpy as np
from sklearn.metrics import mean_squared_error

def evaluate_model(model, data):
    """ Calculate evaluation metrics such as RMSE """
    predictions = model.predict()
    actual = data['Close_diff'].dropna()
    rmse = np.sqrt(mean_squared_error(actual, predictions))
    return rmse


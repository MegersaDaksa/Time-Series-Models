import numpy as np
from sklearn.metrics import mean_squared_error

def evaluate_model(model, data):
    """ Calculate evaluation metrics such as RMSE """
    predictions = model.predict()
    actual = data['Close_diff'].dropna()
    rmse = np.sqrt(mean_squared_error(actual, predictions))
    return rmse

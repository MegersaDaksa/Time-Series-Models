from sklearn.metrics import mean_squared_error

def evaluate_model(model_fit, test_data):
    predictions = model_fit.forecast(steps=len(test_data))
    rmse = mean_squared_error(test_data, predictions, squared=False)
    return rmse

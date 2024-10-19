def predict_future_prices(model, steps=10):
    """ Predict future prices based on the ARIMA model """
    forecast = model.forecast(steps=steps)
    return forecast

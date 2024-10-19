def predict_future_prices(model, end_date):
    """ Predict future prices based on the ARIMA model """
    current_date = pd.to_datetime(model.index[-1]).tz_localize(None)
    end_date = pd.to_datetime(end_date).tz_localize(None)
    if end_date <= current_date:
        raise ValueError("End date must be after the last date in the model data.")
    
    steps = (end_date - current_date).days
    forecast = model.get_forecast(steps=steps)
    return forecast.predicted_mean
def run_workflow():
    from src.data.data_pipeline import run_etl
    from src.models.arima_model import build_arima_model, predict_future

    # ETL Process
    data = run_etl()

    # Build Model
    model = build_arima_model(data)

    # Predict Future Values
    future_predictions = predict_future(model, steps=10)
    print(future_predictions)

if __name__ == '__main__':
    run_workflow()

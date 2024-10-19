import unittest
from src.models.arima_model import build_arima_model
from src.data.data_pipeline import run_etl

class TestARIMAModel(unittest.TestCase):
    def test_arima_model(self):
        data = run_etl()
        model = build_arima_model(data)
        self.assertIsNotNone(model)

if __name__ == '__main__':
    unittest.main()

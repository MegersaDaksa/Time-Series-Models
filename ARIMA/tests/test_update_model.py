import unittest
from src.update_model import update_arima_model

class TestUpdateModel(unittest.TestCase):
    def test_model_update(self):
        old_model = train_arima_model([test_data])
        new_data = [new_test_data]
        updated_model = update_arima_model(new_data, old_model)
        self.assertIsNotNone(updated_model)

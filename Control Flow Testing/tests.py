import unittest
from taxi_rates import calculate_rate

class TestTaxiRates(unittest.TestCase):

    def test_negative_distance(self):
        with self.assertRaises(ValueError):
            calculate_rate(-1, 1)

    def test_invalid_car_type(self):
        with self.assertRaises(ValueError):
            calculate_rate(1, 0)

    def test_valid_input_one_km(self):
        rate = calculate_rate(1, 1)
        self.assertEqual(rate, 20000)

    def test_valid_input_three_km(self):
        rate = calculate_rate(3, 1)
        self.assertEqual(rate, 48000)

if __name__ == '__main__':
    unittest.main()
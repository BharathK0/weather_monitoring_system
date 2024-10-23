import unittest
from src.weather_fetcher import fetch_weather

# test/test_weather_fetcher.py

class TestWeatherFetcher(unittest.TestCase):
    def test_fetch_weather(self):
        city = "Delhi"
        result = fetch_weather(city)
        self.assertIn('temp', result, "Temperature should be present in the weather data")
        self.assertIn('feels_like', result, "Feels_like temperature should be present in the weather data")
        self.assertIn('weather', result, "Main weather condition should be present in the weather data")

if __name__ == '__main__':
    unittest.main()
import unittest
from weather_aggregator import WeatherAggregator

# test/test_weather_aggregator.py

class TestWeatherAggregator(unittest.TestCase):
    def setUp(self):
        self.aggregator = WeatherAggregator()

    def test_aggregate(self):
        # Simulate weather data for a city over a day
        weather_data = [
            {'temp': 30, 'feels_like': 32, 'weather': 'Clear', 'timestamp': '2024-10-22 09:00:00'},
            {'temp': 35, 'feels_like': 37, 'weather': 'Clear', 'timestamp': '2024-10-22 12:00:00'},
            {'temp': 28, 'feels_like': 30, 'weather': 'Clear', 'timestamp': '2024-10-22 15:00:00'}
        ]

        # Aggregate weather data for the day
        for data in weather_data:
            self.aggregator.aggregate('Delhi', data)

        # Fetch the daily summary
        summary = self.aggregator.get_daily_summary('Delhi')

        # Test the summary values
        self.assertAlmostEqual(summary['average_temp'], 31, delta=1, msg="Average temperature calculation is incorrect")
        self.assertEqual(summary['max_temp'], 35, "Maximum temperature should be 35")
        self.assertEqual(summary['min_temp'], 28, "Minimum temperature should be 28")
        self.assertEqual(summary['dominant_weather'], 'Clear', "Dominant weather should be 'Clear'")

if __name__ == '__main__':
    unittest.main()
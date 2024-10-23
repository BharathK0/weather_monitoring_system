from collections import defaultdict
import datetime

class WeatherAggregator:
    def __init__(self):
        self.daily_data = defaultdict(list)

    def aggregate(self, city, weather_data):
        date = weather_data['timestamp'].split()[0]
        self.daily_data[city].append(weather_data)

    def get_daily_summary(self, city):
        city_data = self.daily_data[city]
        if not city_data:
            return None
        
        avg_temp = sum(data['temp'] for data in city_data) / len(city_data)
        max_temp = max(data['temp'] for data in city_data)
        min_temp = min(data['temp'] for data in city_data)
        dominant_weather = max(set([data['weather'] for data in city_data]), key=[data['weather'] for data in city_data].count)
        
        return {
            'average_temp': avg_temp,
            'max_temp': max_temp,
            'min_temp': min_temp,
            'dominant_weather': dominant_weather,
            'date': city_data[0]['timestamp'].split()[0]
        }
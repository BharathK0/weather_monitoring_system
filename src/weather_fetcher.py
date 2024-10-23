import requests
import json
import time
from datetime import datetime

# Load configuration
with open('config/config.json') as config_file:
    config = json.load(config_file)

API_KEY = config['api_key']
CITIES = config['cities']  # List of cities from config file
FETCH_INTERVAL = config['fetch_interval']  # Fetch interval from config file
UNIT = config['temperature_unit']  # metric for Celsius, imperial for Fahrenheit

def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={UNIT}"
    response = requests.get(url)
    return response.json()

def main():
    # Define how many times you want to fetch weather updates
    max_iterations = 5  # Number of times the loop will run
    iterations = 0  # Initialize counter

    while iterations < max_iterations:
        weather_data = {}  # To store data for all cities
        for city in CITIES:
            # Fetch weather data for each city
            data = fetch_weather(city)
            weather_data[city] = {
                'temp': data['main']['temp'],
                'feels_like': data['main']['feels_like'],
                'weather': data['weather'][0]['main'],
                'timestamp': datetime.fromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S')
            }
        print(weather_data)  # Print or process the fetched weather data

        # Increment the counter for iterations
        iterations += 1
        time.sleep(FETCH_INTERVAL)  # Wait for the next interval (e.g., 5 minutes)

if __name__ == "__main__":
    main()

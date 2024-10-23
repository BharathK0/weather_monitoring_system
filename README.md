# Weather Monitoring System

## Project Overview
The Weather Monitoring System is designed to provide real-time weather monitoring using the OpenWeatherMap API. It fetches, aggregates, and visualizes weather data, and can alert users when certain thresholds are met.

## Prerequisites
- Python
- pip
- Docker (optional)

## Installation Steps
```bash
# Clone the repository
git clone https://github.com/BharathK0/weather_monitoring_system.git

# Navigate to the project directory
cd weather-monitoring-system

# Install dependencies
pip install -r requirements.txt

# Run the application
python src/weather_fetcher.py
```

## Configuration
To configure the API key and other settings, edit the `config/config.json` file. Ensure you have a valid API key from OpenWeatherMap.

## Features
- Real-time weather data fetching
- Daily rollup and aggregation
- Threshold alerting
- Visualization

## Tests
To run the test cases, use the following command:
```bash
# Run tests
python -m unittest discover -s test
```

## License
This project is licensed under the MIT License.











































import matplotlib.pyplot as plt

def plot_summary(city, daily_summaries):
    dates = [summary['date'] for summary in daily_summaries]
    temps = [summary['average_temp'] for summary in daily_summaries]
    
    plt.plot(dates, temps, marker='o', label=f'{city} Avg Temp')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title(f'{city} Temperature Trends')
    plt.legend()
    plt.show()
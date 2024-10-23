class AlertingSystem:
    def __init__(self, threshold_temp):
        self.threshold_temp = threshold_temp
        self.previous_temp = {}

    def check_threshold(self, city, current_temp):
        if city not in self.previous_temp:
            self.previous_temp[city] = current_temp
            return
        
        if current_temp > self.threshold_temp and self.previous_temp[city] > self.threshold_temp:
            print(f"ALERT: {city} has exceeded {self.threshold_temp}°C for two consecutive readings!")
        
        self.previous_temp[city] = current_temp
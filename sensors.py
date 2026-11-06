import random

class TemperatureSensor:

    def __init__(self, location):
        self.location = location
        
    def read(self):
        # Simulate reading temperature from a sensor
        return round(random.uniform(68, 75), 1)  # Temperature in Fahrenheit

    def display(self):
        return f"Sensor Location: {self.location} | Temperature: {self.read()}°F"

lobby_sensor = TemperatureSensor('Lobby')
mechanical_room_sensor = TemperatureSensor('Mechanical Room')

print(lobby_sensor.display())
print(mechanical_room_sensor.display())
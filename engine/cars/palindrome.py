from Car import Car
from engines.SternmanEngine import SternmanEngine
from batteries.SpindlerBattery import SpindlerBattery
from tires.CarriganTire import CarriganTire

class Palindrome(Car):
    def __init__(self,sensorValues,current_date, last_service_date, warning_indicator_on):
        Palindrome_engine=SternmanEngine(warning_indicator_on)
        Palindrome_battery=SpindlerBattery(current_date, last_service_date)
        Palindrome_tire=CarriganTire(sensorValues)
        super().__init__(Palindrome_engine, Palindrome_battery, Palindrome_tire)
        self.engine=Palindrome_engine
        self.battery=Palindrome_battery
        self.tire=Palindrome_tire

    def needs_service(self):
        return super().needs_service;
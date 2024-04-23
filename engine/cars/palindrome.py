from model.Car import Car
from engines.SternmanEngine import SternmanEngine
from batteries.SpindlerBattery import SpindlerBattery

class Palindrome(Car):
    def __init__(self,last_service_date, warning_indicator_on):
        Palindrome_engine=SternmanEngine(warning_indicator_on)
        Palindrome_battery=SpindlerBattery(last_service_date)
        super().__init__(Palindrome_engine, Palindrome_battery)
        self.engine=Palindrome_engine
        self.battery=Palindrome_battery

    def needs_service(self):
        return super().needs_service;
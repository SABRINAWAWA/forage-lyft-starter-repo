from model.Car import Car
from engines.WilloughbyEngine import WilloughbyEngine
from batteries.SpindlerBattery import SpindlerBattery

class Glissage(Car):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        Glissage_engine=WilloughbyEngine(current_mileage, last_service_mileage)
        Glissage_battery=SpindlerBattery(current_date, last_service_date)
        super().__init__(Glissage_engine, Glissage_battery)
        self.engine=Glissage_engine
        self.battery=Glissage_battery

    def needs_service(self):
        return super().needs_service;
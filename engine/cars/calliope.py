from model.Car import Car
from engines.CapuletEngine import CapuletEngine
from batteries.SpindlerBattery import SpindlerBattery

class Calliope(Car):
    def __init__(self, current_mileage, last_service_mileage, last_service_date):
        Calliope_engine=CapuletEngine(current_mileage, last_service_mileage)
        Calliope_battery=SpindlerBattery(last_service_date)
        super().__init__(Calliope_engine, Calliope_battery)
        self.engine=Calliope_engine
        self.battery=Calliope_battery

    def needs_service(self):
        return super().needs_service;

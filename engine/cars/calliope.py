from model.Car import Car
from engines.CapuletEngine import CapuletEngine
from batteries.SpindlerBattery import SpindlerBattery

class Calliope(Car):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        Calliope_engine=CapuletEngine(current_mileage, last_service_mileage)
        Calliope_battery=SpindlerBattery(current_date, last_service_date)
        super().__init__(Calliope_engine, Calliope_battery)
        self.engine=Calliope_engine
        self.battery=Calliope_battery

    def needs_service(self):
        return super().needs_service;

from model.Car import Car
from engines.CapuletEngine import CapuletEngine
from batteries.NubbinBattery import NubbinBattery

class Thovex(Car):
    def __init__(self,current_date, last_service_date, current_mileage, last_service_mileage):
        Thovex_engine=CapuletEngine(current_mileage, last_service_mileage)
        Thovex_battery=NubbinBattery(current_date, last_service_date)
        super().__init__(Thovex_engine, Thovex_battery)
        self.engine=Thovex_engine
        self.battery=Thovex_battery

    def needs_service(self):
        return super().needs_service;

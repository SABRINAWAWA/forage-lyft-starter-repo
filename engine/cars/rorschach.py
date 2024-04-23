from model.Car import Car
from engines.WilloughbyEngine import WilloughbyEngine
from batteries.NubbinBattery import NubbinBttery

class Rorschach(Car):
    def __init__(self,current_mileage, last_service_mileage, last_service_date):
        Rorschach_engine=WilloughbyEngine(current_mileage, last_service_mileage)
        Rorschach_battery=NubbinBttery(last_service_date)
        super().__init__(Rorschach_engine, Rorschach_battery)
        self.engine=Rorschach_engine
        self.battery=Rorschach_battery

    def needs_service(self):
        return super().needs_service;
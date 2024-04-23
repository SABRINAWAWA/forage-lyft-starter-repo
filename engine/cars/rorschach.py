from Car import Car
from engines.WilloughbyEngine import WilloughbyEngine
from batteries.NubbinBattery import NubbinBttery
from tires.OctoprimeTire import OctoprimeTire

class Rorschach(Car):
    def __init__(self,sensorValues, current_date, last_service_date, current_mileage, last_service_mileage):
        Rorschach_engine=WilloughbyEngine(current_mileage, last_service_mileage)
        Rorschach_battery=NubbinBttery(current_date, last_service_date)
        Rorschach_tire=OctoprimeTire(sensorValues)
        super().__init__(Rorschach_engine, Rorschach_battery, Rorschach_tire)
        self.engine=Rorschach_engine
        self.battery=Rorschach_battery
        self.tire=Rorschach_tire

    def needs_service(self):
        return super().needs_service;
from Car import Car
from engines.CapuletEngine import CapuletEngine
from batteries.NubbinBattery import NubbinBattery
from tires.OctoprimeTire import OctoprimeTire
class Thovex(Car):
    def __init__(self,sensorValues, current_date, last_service_date, current_mileage, last_service_mileage):
        Thovex_engine=CapuletEngine(current_mileage, last_service_mileage)
        Thovex_battery=NubbinBattery(current_date, last_service_date)
        Thovex_tire=OctoprimeTire(sensorValues)
        super().__init__(Thovex_engine, Thovex_battery, Thovex_tire)
        self.engine=Thovex_engine
        self.battery=Thovex_battery
        self.tire=Thovex_tire

    def needs_service(self):
        return super().needs_service;

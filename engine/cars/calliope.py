from Car import Car
from engines.CapuletEngine import CapuletEngine
from batteries.SpindlerBattery import SpindlerBattery
from tires.CarriganTire import CarriganTire

class Calliope(Car):
    def __init__(self, sensorValues, current_date, last_service_date, current_mileage, last_service_mileage):
        Calliope_engine=CapuletEngine(current_mileage, last_service_mileage)
        Calliope_battery=SpindlerBattery(current_date, last_service_date)
        Carrigan_tire=CarriganTire(sensorValues)
        super().__init__(Calliope_engine, Calliope_battery, Carrigan_tire)
        self.engine=Calliope_engine
        self.battery=Calliope_battery
        self.tire=Carrigan_tire

    def needs_service(self):
        return super().needs_service;

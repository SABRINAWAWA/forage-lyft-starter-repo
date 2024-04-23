from Car import Car
from engines.WilloughbyEngine import WilloughbyEngine
from batteries.SpindlerBattery import SpindlerBattery
from tires.CarriganTire import CarriganTire

class Glissage(Car):
    def __init__(self, sensorValues, current_date, last_service_date, current_mileage, last_service_mileage):
        Glissage_engine=WilloughbyEngine(current_mileage, last_service_mileage)
        Glissage_battery=SpindlerBattery(current_date, last_service_date)
        Glissage_tire=CarriganTire(sensorValues)
        super().__init__(Glissage_engine, Glissage_battery, Glissage_tire)
        self.engine=Glissage_engine
        self.battery=Glissage_battery
        self.tire=Glissage_tire

    def needs_service(self):
        return super().needs_service;
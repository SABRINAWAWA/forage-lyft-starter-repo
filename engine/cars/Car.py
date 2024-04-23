from engines.Engine import Engine
from batteries.Battery import Battery
from tires.Tire import Tire
class Car(Engine, Battery, Tire):
    def __init__(self, engine, battery, tire):
        self.engine = engine
        self.battery = battery
        self.tire=tire
    def needs_service(self):
        return self.engine.need_services() or self.battery.need_services() or self.tire.need_services()

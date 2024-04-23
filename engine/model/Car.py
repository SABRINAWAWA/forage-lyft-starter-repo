from Engine import Engine
from Battery import Battery

class Car(Engine, Battery):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery
    def needs_service(self):
        return self.engine.need_services() or self.battery.need_services()

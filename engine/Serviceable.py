from model.Car import Car
class Serviceable(Car):
    def __init__(self,  car):
        self.car= car

    def needs_service(self):
        return self.car.needs_service()

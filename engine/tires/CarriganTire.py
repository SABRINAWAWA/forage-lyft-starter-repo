from Tire import Tire

class CarriganTire(Tire):
    def __init__(self, sensorValues):
        super.__init__(sensorValues)
        self.sensorValues = sensorValues

    def needs_service(self):
        for value in self.sensorsValues:
            if value>=0.9:
                return True
        return False

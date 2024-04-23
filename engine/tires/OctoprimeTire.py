from Tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, sensorValues):
        super.__init__(sensorValues)
        self.sensorValues = sensorValues

    def needs_service(self):
        return sum(self.sensorsValues)>=3

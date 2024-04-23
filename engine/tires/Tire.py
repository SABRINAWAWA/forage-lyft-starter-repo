from abc import ABC, abstractmethod

class Tire(ABC):
    def __init__(self, sensorsValues):
        self.sensorsValues=sensorsValues

    @abstractmethod
    def needs_service(self):
        pass

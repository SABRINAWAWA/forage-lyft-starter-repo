from Battery import Battery
from datetime import datetime

class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        super.__init__(current_date, last_service_date)

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 3)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False


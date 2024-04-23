from datetime import datetime

from model.Engine import Engine
from model.Battery import Battery
from model.Car import Car
from cars.calliope import Calliope
from cars.glissade import Glissade
from cars.palindrome import Palindrome
from cars.rorschach import Rorschach
from cars.thovex import Thovex

class CarFactory():
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage): 
        return Calliope(current_date, last_service_date, current_mileage, last_service_mileage)
    
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage): 
        return Glissade(current_date, last_service_date, current_mileage, last_service_mileage)
    
    def create_palindrome(current_date, last_service_date, warning_light_on): 
        return Palindrome(current_date, last_service_date, warning_light_on)
    
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage): 
        return Rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
    
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage): 
        return Thovex(current_date, last_service_date, current_mileage, last_service_mileage)

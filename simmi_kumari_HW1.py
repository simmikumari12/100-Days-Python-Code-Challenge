class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

class Car:
    def __init__(self, car_name, location, cost_per_mile):
        self.car_name = car_name
        self.cost_per_mile = cost_per_mile
        Location.__init__(self, location)
        
class Passenger:
    pass

class RideSharingApp:
    pass
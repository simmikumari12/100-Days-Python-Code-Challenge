class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

class Car(Location):
    def __init__(self, car_name, location, cost_per_mile):
        self.car_name = car_name
        self.cost_per_mile = cost_per_mile
        Location.__init__(self, location)
        
    def __str__(self):
        return f"[{self.car_name}, {self.location}, {self.cost_per_mile}]"
    
    def move_to(self,new_x, new_y):
        return Location.__init__(new_x,new_y)

class Passenger(Location):
    def __init__(self, passenger_name, location):
        self.passenger_name = passenger_name
        Location.__init__(self, location)

    def __str__(self):
        return f"[{self.car_name}, {self.location}, {self.cost_per_mile}]"
    
    def move_to(self,new_x, new_y):
        return Location.__init__(new_x,new_y)


class RideSharingApp:
    def __init__(self):
        cars = []
        passengers = []

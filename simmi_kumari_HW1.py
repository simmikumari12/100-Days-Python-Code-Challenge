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
       self.location = f"({new_y}, {new_y})"
       return self.location

class Passenger(Location):
    def __init__(self, passenger_name, location):
        self.passenger_name = passenger_name
        Location.__init__(self, location)

    def __str__(self):
        return f"[{self.car_name}, {self.location}, {self.cost_per_mile}]"
    
    def move_to(self,new_x, new_y):
        return Location.__init__(new_x,new_y)


class RideSharingApp(Car): 
    def __init__(self):
        self.cars = []
        self.passengers = []

    def add_car(self, car):
        return self.cars.append(car)
    
    def add_passenger(self, passenger):
        return self.passengers.append(passenger)
    
    def remove_car(self, car):
        return self.cars.pop(car)
    
    def remove_passenger(self, passenger):
        return self.passengers.pop(passenger)        

    def find_cheapest_car(self):
        return min(self.cost_per_mile)
    
    def find_nearest_car(self, passenger):
        pass


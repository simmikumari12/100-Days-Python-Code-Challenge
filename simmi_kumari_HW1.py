import math

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
        super().__init__(self, location)
        
    def __str__(self):
        return f"[{self.car_name}, {self.location}, {self.cost_per_mile}]"
    
    def move_to(self,new_x, new_y):
       self.location.x = new_x
       self.location.y = new_y

class Passenger(Location):
    def __init__(self, passenger_name, location):
        self.passenger_name = passenger_name
        Location.__init__(self, location)

    def __str__(self):
        return f"[{self.car_name}, {self.location}, {self.cost_per_mile}]"
    
    def move_to(self,new_x, new_y):
        self.location = f"({new_x}, {new_y})"
        return self.location


class RideSharingApp(Car): 
    def __init__(self):
        self.cars = []
        self.passengers = []

    def add_car(self, car):
        return self.cars.append(car)
    
    def add_passenger(self, passenger):
        return self.passengers.append(passenger)
    
    def remove_car(self, car):
        return self.cars.remove(car)
    
    def remove_passenger(self, passenger):
        return self.passengers.remove(passenger)        

    def find_cheapest_car(self):
        return min(self.cost_per_mile)
    
    def find_nearest_car(self, passenger):
        if self.cars:
            nearest_car = min(self.cars, key=lambda car: self.calculate_distance(car.location, passenger.location))
            distance = self.calculate_distance(nearest_car.location, passenger.location)
            print(f"Nearest car for {passenger.passenger_name}: {nearest_car.car_name}, Distance: {distance:.2f}")

    def calculate_distance(self, loc1, loc2):
        return math.sqrt((loc1.x - loc2.x) ** 2 + (loc1.y - loc2.y) ** 2)


a = RideSharingApp()
print(a)
import requests
import sys
import cred

class City:
    def __init__(self, name, lat, lon, units = "metric"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()

    def get_data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid={cred.api_key}")
        except:
            print("Please check your internet connection and Try Again!")
            sys.exit()

        response_json = response.json()
        self.temp = response_json["main"]["temp"]
        self.temp_min = response_json["main"]["temp_min"]
        self.temp_max = response_json["main"]["temp_max"]

    def print_data(self):
        unit_symbol = "C"
        if self.units == "imperial":
            unit_symbol = "F"

        print(f"\n{self.name}:")
        print(f"Current Temperature: {self.temp}°{unit_symbol}")
        print(f"Today's high: {self.temp_max}°{unit_symbol}")
        print(f"Today's low: {self.temp_min}°{unit_symbol}\n")

city1 = City("Gopalganj", 26.4606, 84.4402)
city1.print_data()

city2 = City("Bengaluru", 12.9716, 77.5946)
city2.print_data()

city3 = City("Atlanta", 33.7501, -84.3885, "imperial")
city3.print_data()








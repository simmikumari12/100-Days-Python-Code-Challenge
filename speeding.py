import sys

speed_limit = int(input("Please enter the speed limit for the road: "))
recorded_speed = int(input("Please enter the vehicle's recorded peed: "))

conditional_value = recorded_speed - speed_limit

if 10 < conditional_value :
    ticket_price = 50

elif 6 < conditional_value <= 20:
    ticket_price = 75

elif conditional_value <40:
    ticket_price = 150

elif conditional_value > 40:
    ticket_price = 300
else:
    ticket_price = 0
    print("There is no fine")
    sys.exit()
print(f"The speeding fine is ${ticket_price}.")
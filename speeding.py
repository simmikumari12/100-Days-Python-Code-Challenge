import sys

speed_limit = int(input("Please enter the speed limit for the road: "))
recorded_speed = int(input("Please enter the vehicle's recorded speed: "))

conditional_value = speed_limit - recorded_speed

if 10 < conditional_value :
    ticket_price = 50
elif 6 < conditional_value <= 20:
    ticket_price = 75
elif 21 <= conditional_value <40:
    print(conditional_value)
    ticket_price = 150
elif conditional_value >= 40:
    ticket_price = 300
else:
    print("There is no fine")
    sys.exit()
print(f"The speeding fine is ${ticket_price}.")


#too slow speed will make traffic jam so if the speed limit is 23 and the driving speed is 3, there will be fine of $50
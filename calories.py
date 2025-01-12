import sys

age = 0
while age <= 0:
    try:
        age = int(input("Age = "))
    except:
        print("Invalid Age!")

weight = 0
while weight <= 0:
    try:
        weight = int(input("Weight = "))     
    except:
        print("Invalid age!")

while True:
    try:
        weight = int(input("Weight = "))     
    except:
        print("Invalid Weight!")
        heart_rate = int(input("Heart Rate = "))
        time = int(input("Time = "))
 
# calories = ((age * 0.2757 + weight * 0.03295 + heart_rate * 1.0781 - 75.4991) * time)/ 8.368
# print(f"Calories burned: {calories:.2f}")
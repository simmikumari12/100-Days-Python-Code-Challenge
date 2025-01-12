age = int(input("Age = "))
weight = int(input("Weight = "))
heart_rate = int(input("Heart Rate = "))
time = int(input("Time = "))

calories = ((age * 0.2757 + weight * 0.03295 + heart_rate * 1.0781 - 75.4991) * time)/ 8.368

print(f"Calories burned: {calories:.2f}")
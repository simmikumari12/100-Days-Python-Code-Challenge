# For this program, you will need to adjust the input values by dividing all inputs by the largest value. The first input begins 
# with an integer indicating the number of floating-point values that will follow.

num = int(input("Please enter the number of floating point values: "))
values = []
for _ in range(num):
    values.append(float(input("Please enter a floating-point value: "))) 

max_value  = max(values)
for value in values:
    print(f"Normalised floating-point Values: {(value/max_value):0.2f}")
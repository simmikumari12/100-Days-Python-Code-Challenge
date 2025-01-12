# To find volume of a shphera and factorial of randomly generated number between 1 - 10

import math
import random
import sys

r = sys.argv[1]
try:
    radius = int(r)  
except ValueError:
    print("\nInvalid Radius")
else:
    if radius > 0:
        volume = (4 * math.pi * (radius ** 3))/3
        print(f"\nVolume of sphere with radius {radius} = {volume:0.2f} sq units")
    else:
        print("\nInvalid Radius")

num = random.randint(1,10)
print(f"{num}! = {math.factorial(num)}\n")

# To find volume of a shphera and factorial of randomly generated number between 1 - 10

import math
import random
import sys

r = sys.argv[1]
radius = int(r)

volume = (4 * math.pi * (radius ** 3))/3
print(f"\nVolume of sphere with radius {radius} = {volume:0.2f} sq units")

num = random.randint(1,10)
print(f"{num}! = {math.factorial(num)}\n")

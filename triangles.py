import sys

if len(sys.argv) > 4:
    print("Too many Arguments!")
    sys.exit()
if len(sys.argv) < 4:
    print("Too Few Arguments!")
    sys.exit()

x = sys.argv[1]
y = sys.argv[2]
z = sys.argv[3]
try:
    a = int(x)
    b = int(y)
    c = int(z)
except ValueError:
    print("Invalid Input")
if a + b <= c:
    print("Invalid length")
    sys.exit()
if a + c <= b:
    print("Invalid length")
    sys.exit()
if b + c <= a:
    print("Invalid length")
    sys.exit()


s = (a + b + c) / 2
print(f"\nPerimeter = {s * 2} sq units")

area = (s * (s-a) * (s-b) * (s-c))**(1/2)
print(f"Area = {area:0.3f} sq unit\n")

longest = a
if  a < b:
    longest = b
elif a < c:
    longest = c
else:
    longest = a
print(longest)

if a == longest:
    right_hand_side = c * c + b * b 
elif b == longest:
    right_hand_side = a * a + c * c
else: 
    right_hand_side = a * a + b * b 
    
left_hand_side = longest * longest
if right_hand_side == left_hand_side:
    print("Right Triangle")
elif right_hand_side < left_hand_side:
    print("Obtuse Triangle")
else:
    print("Acute Triangle")
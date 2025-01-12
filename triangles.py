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
print(s)

area = (s * (s-a) * (s-b) * (s-c))**(1/2)
print(area)
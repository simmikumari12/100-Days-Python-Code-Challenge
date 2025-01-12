import sys
if len(sys.argv) > 4:
    print("Too many Arguments!")
    sys.exit()
if len(sys.argv) < 4:
    print("Too Few Arguments!")
    sys.exit()
    
a = sys.argv[1]
b = sys.argv[2]
c = sys.argv[3]

print(a, b, c)
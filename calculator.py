import sys

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def add(self, b):
        return self + b
    
    def subtract(self, b):
        return self - b
    
    def multiply(self, b):
        return self * b

    def divide(self, b):
        return self / b
    
    def modulo(self, b):
        return self % b
    
    def floorDivision(self, b):
        return self // b
    
    def exponent(self, b):
        return self ** b
     
if len(sys.argv) > 4:
    print("Too many arguments")
    sys.exit()
elif len(sys.argv) < 4:
    print("Too few arguments")
    sys.exit()

try:
    x = float(sys.argv[1]) 
    y = float(sys.argv[3])
except ValueError:
    print("Invalid Input")
    sys.exit() 

operation = sys.argv[2]
if operation not in ["+", "-", "*", "/", "%", "//", "**"]:
    print("Invalid Operator")
    sys.exit()

def perform_operator():
    if operation == "+":
        return Calculator.add(x,y)
    elif operation == "-":
        return Calculator.subtract(x,y)
    elif operation == "*":
        return Calculator.multiply(x,y)
    elif operation == "/":
        return Calculator.divide(x,y)
    elif operation == "%":
        return Calculator.modulo(x,y)
    elif operation == "//":
        return Calculator.floorDivision(x,y)
    elif operation == "**":
        return Calculator.exponent(x,y)
    else:
        return "Sorry, Could not perform the operation :("
    
def main():
    print(f"{sys.argv[1]} {sys.argv[2]} {sys.argv[3]} = {perform_operator()}")
    
if __name__ == "__main__":
   main()
    
    
    
    
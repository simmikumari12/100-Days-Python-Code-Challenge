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
    
print(Calculator.add(3,7))
print(Calculator.subtract(3,7))
print(Calculator.multiply(3,7))
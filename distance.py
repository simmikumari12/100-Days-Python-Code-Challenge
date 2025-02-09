# area between two points in the cartessian plain

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def distance(self, other):
    return ((self.x  - other.x)**2 + (self.y - other.y)**2) ** (1/2)
  
def main():
    x1, y1 = input("Enter any point(x,y): ").split(",")
    p1 = Point(float(x1), float(y1))

    x2, y2 = input("Enter another point(x, y): ").split(",")
    p2 = Point(float(x2), float(y2))

    print(f"Distance between ({x1}, {y1}) and ({x2}, {y2}) = {p1.distance(p2):0.2} units")

if __name__ == "__main__":
   main()
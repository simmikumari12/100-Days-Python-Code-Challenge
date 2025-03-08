import sys

def main():
  frac = input("Fraction: ")
  value = convert(frac)
  print(gauge(value))

def convert(fraction):
  try:
    num, denom = fraction.split("/")
    x = int(num)
    y = int(denom)
  except ValueError:
    sys.exit()

  if x > y:
    raise ValueError(sys.exit())
    
  try:
    percen = (x/y)*100
  except ZeroDivisionError:
    sys.exit()

  return round(percen)

def gauge(percentage):
  if percentage <= 1:
    return "E"
  elif percentage >= 99:
    return "F"
  else:
    return f"{percentage}%"

if __name__ == "__main__":
    main()
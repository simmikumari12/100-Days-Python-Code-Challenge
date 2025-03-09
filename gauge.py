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
  except ValueError as e:
    raise e

  if x > y:
    if y == 0:
      raise ZeroDivisionError()
    else:
        raise ValueError()
    
    
  try:
    percen = (x/y)*100
  except ZeroDivisionError as e:
    raise e
  
  else:
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
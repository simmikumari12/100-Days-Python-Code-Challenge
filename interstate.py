import sys
try:
    number = int(input("Please enter an interstate number: "))
except ValueError:
    print("Invalid Input!")
    sys.exit()

if number < 0 or number > 1000:
    print("Invalid Input!")
    sys.exit()

def direction_decider(value):
    if value % 2 == 0:
        return "east/west"
    else:
        return "north/south"

if 1 < number < 99:
    print(f"I-{number} is primary, going {direction_decider(number)}")


if 100 < number < 999:
    last_digits = number % 100 
    if last_digits == 00:
        print(f"{number} is not a valid interstate highway number.")
        sys.exit()

    print(f"I-{number} is auxiliary, serving I-{last_digits}, going {direction_decider(last_digits)}")


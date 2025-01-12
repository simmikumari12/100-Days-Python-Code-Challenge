number = int(input("Please enter an interstate number: "))

if 1 < number < 99:
    pass


if 100 < number < 999:
    last_digits = number % 100 
    if last_digits == 00:
        print(f"{number} is not a valid interstate highway number.")
    if last_digits % 2 == 0:
        direction = "east/west"
    else:
        direction = "north/south"
    print(f"I-{number} is auxiliary, serving I-{last_digits}, going {direction}")


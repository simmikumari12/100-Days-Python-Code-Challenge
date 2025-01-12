cents = int(input("Please Enter a number of cents: "))

quarters = cents // 25
print("quarters", quarters)
dimes = (cents - quarters * 25)//10
print("dimes:",dimes)

nickels = (cents - quarters - dimes)//5
print("nickels:",nickels)
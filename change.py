cents = int(input("Please Enter a number of cents: "))

quarters = cents // 25
print("quarters", quarters)
dimes = (cents - quarters * 25)//10
print("dimes:",dimes)

nickels = (cents - quarters * 25 - dimes * 10)//5
print("nickels:",nickels)

pennies = (cents - quarters * 25 - dimes * 10 - nickels * 5)//1
print("pennies:",pennies)


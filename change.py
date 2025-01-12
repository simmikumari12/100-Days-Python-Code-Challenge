cents = int(input("Please Enter a number of cents: "))

quarters = cents // 25
dimes = (cents - quarters * 25)//10
nickels = (cents - quarters * 25 - dimes * 10)//5
pennies = (cents - quarters * 25 - dimes * 10 - nickels * 5)//1

print(f"Coins: {quarters} quarters, {dimes} dimes, {nickels} nickels, {pennies} pennies")

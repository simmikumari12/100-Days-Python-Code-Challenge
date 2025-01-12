
number = input("Please enter your phone number: ")
if len(number) != 10:
    print("Invalid number!")
n = int(number)
print(f"Phone Number: ({n // (10**7)}) {} - {n % (10 ** 4)}")
    


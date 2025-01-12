import sys

while True:
    number = input("Please enter your phone number: ")
    if len(number) == 10:
        break
        # print("Invalid number!")

try:
    n = int(number)
except:
    print("Invalid Number")
    sys.exit()
        
print(f"Phone Number: ({n // 10000000}) {(n%10000000)//10000}-{n % 10000}")
    


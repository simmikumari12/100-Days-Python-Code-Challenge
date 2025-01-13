password = input("Please Enter Your Password: ").replace("o", "0").replace("i", "1").replace("e", "3").replace("A", "4").replace("B", "8").replace("s", "$")
print(f"Your new strong password is: {password}!")

password = input("Please Enter Your Password: ")
for character in password:
    if character == 'o':
        character = 0       
    elif character == 'i':
        character = 1
    elif  character == 'e':
        character = 3
    elif character == 'A':
        character = 4
    elif  character == 'B':
        character = 8
    elif  character == 's':
        character = '$'
    print(character,end="")
print(password)
print("\n")

import random 
from bidict import bidict


def main():
    user = input("Choose between Snake, Gun and Water\n").lower()
    possible_values = bidict({"snake": 1, "water": 2, "gun": 3})
    value = possible_values[user]
    machine = random.randint(1,4)
    print("Please Wait Entering My Value:")
    print(f"{possible_values.inv[machine]}")

    if machine == 1: # machine gave snake
        if value == 1:
            print("Game Draw!")
        elif value == 2:
            print("You Lost!")
        elif value == 3:
            print("You Won!")
        else:
            print("Invalid Input")


    if machine == 2: #machine gave water
        if value == 2:
            print("Game Draw!")
        elif value == 3:
            print("You Lost!")
        elif value == 1:
            print("You Won!")
        else:
            print("Invalid Input")

    if machine == 3: #machine gave gun
        if value == 3:
            print("Game Draw!")
        elif value == 1:
            print("You Lost!")
        elif value == 2:
            print("You Won!")
        else:
            print("Invalid Input")    

if __name__ == "__main__":
    main()
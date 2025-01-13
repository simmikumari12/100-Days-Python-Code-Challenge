import random

def main():
    print("Guess the number in 10 attempts!")
    random_num = random.randint(1,100)
    n = 0
    while True:
        guessed_num = int(input(f"Guess:"))
        if guessed_num > random_num:
            print("Too high, Try Again!")
        elif guessed_num < random_num:
            print("Too low, Try again!")
        n = n + 1
        if guessed_num == random_num:
            print("You guessed correctly!")
            break
        elif n == 10:
            print("Out of attempts :(")
            break
if __name__ == "__main__":
    main()
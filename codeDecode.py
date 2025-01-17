import random
import string

def main():
    ans = input("Code or Decode? ").lower()
    if ans == "code":
        print(code())
    elif ans == "decode":
        decode()
        
def code():
    msg = input("Enter your message: ")
    if len(msg) <= 3:
        return f"{msg[::-1]}"
    elif len(msg) > 3:
        first_letter = msg[0]
        coded_value = msg[1:]
        random_choice = []
        characters = string.ascii_letters
        for i in range(6):
            random_choice.append(random.choice(characters))
        return f"Coded Message:{random_choice[0]}{random_choice[1]}{random_choice[2]}{coded_value}{first_letter}{random_choice[3]}{random_choice[4]}{random_choice[5]}"

def decode():
    pass


if __name__ == "__main__":
    main()
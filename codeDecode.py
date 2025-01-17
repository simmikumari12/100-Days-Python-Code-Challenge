import random
import string

def main():
    ans = input("Code or Decode?").lower()
    if ans == "code":
        msg = input("Enter your message: ")
        if len(msg) <= 3:
            print(f"{msg[::-1]}")
        elif len(msg) > 3:
            first_letter = msg[0]
            coded_value = msg[1:]
            characters = string.ascii_letters
            rc1 = random.choice(characters)
            rc2 = random.choice(characters)
            rc3 = random.choice(characters)
            rc4 = random.choice(characters)
            rc5 = random.choice(characters)
            rc6 = random.choice(characters)
            print(f"Coded Message:{rc1}{rc2}{rc3}{coded_value}{first_letter}{rc4}{rc5}{rc6}")



if __name__ == "__main__":
    main()
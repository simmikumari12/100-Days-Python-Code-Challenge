import random
import string

def main():
    ans = input("Code or Decode? ").lower()
    user_msg = input("Enter your message: ")
    if ans == "code":
        print(code(user_msg))
    elif ans == "decode":
        decode(user_msg)
        
def code(msg):    
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

def decode(msg):
    if len(msg) <= 3:
        return f"{msg[::-1]}"
    elif len(msg) > 3:
        m = msg[4:len(msg)-3] 
        last_word = m[len(m)-1]
        return f"DeCoded Message: {last_word}{m}"

    


if __name__ == "__main__":
    main()
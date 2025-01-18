import random
import string

def main():
    ans = input("Code or Decode? ").lower()
    user_msg = input("Enter your message: ").split(" ")
    if ans == "code":
        print(code(user_msg))
    elif ans == "decode":
        print(decode(user_msg))
        
def code(msgs):
    to_return = []
    for msg in msgs:
        if len(msg) <= 3:
            to_return.append(msg[::-1])
        elif len(msg) > 3:
            first_letter = msg[0]
            coded_value = msg[1:]
            random_choice = []
            characters = string.ascii_letters
            for i in range(6):
                random_choice.append(random.choice(characters))
            to_return.append(f"{random_choice[0]}{random_choice[1]}{random_choice[2]}{coded_value}{first_letter}{random_choice[3]}{random_choice[4]}{random_choice[5]}")
    final = " ".join(to_return)
    return final

def decode(msgs):
    to_return = []
    for msg in msgs:
        if len(msg) <= 3:
            to_return.append(msg[::-1])
        elif len(msg) > 3:
            m = msg[3:len(msg)-3] 
            last_word = m[len(m)-1]
            to_return.append(f"{last_word}{m[:len(m)-1]}")
    final = " ".join(to_return)
    return final

if __name__ == "__main__":
    main()
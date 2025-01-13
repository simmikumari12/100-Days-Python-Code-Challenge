def text_filter(str_value):
    banned_words = ["Turkey", "Dog", "Fox", "Cat", "Chicken"]
    for banned_word in banned_words:
        for s in str_value:
            if s == banned_word:
                s = ""
                str_value.remove(banned_words)
    return str_value

def main():
    msgin = input("Input Message: ").title()
    print(f"Output Message: {text_filter(msgin)}")

if __name__ == "__main__":
    main()
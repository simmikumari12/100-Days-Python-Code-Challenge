def main():
    msg = input("Input Message: ").lower()
    print(f"Output Message: {text_filter(msg)}")

def text_filter(sentence):
    banned_words = ["turkey", "dog", "fox", "cat", "chicken"]
    updated = sentence.split(" ")
    to_return = []

    for w in updated:
        if w not in banned_words:
            to_return.append(w)

    return (" ".join(to_return)).title()

if __name__ == "__main__":
    main()
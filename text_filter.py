def main():
    msg = input("Input Message: ")
    print(f"Output Message: {text_filter(msg)}")

def text_filter(sentence):
    banned_words = ["turkey", "dog", "fox", "cat", "chicken"]
    updated = []
    for word in sentence:
        if word != banned_words:
            updated.append(word)

    print(word)


if __name__ == "__main__":
    main()
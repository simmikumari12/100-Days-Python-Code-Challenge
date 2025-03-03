def main():
    words = input()
    build_dictionary(words)

def build_dictionary(words):
    word_ls = words.lower().split(" ")
    word_dict = {}
    for word in word_ls:
        if word in word_dict.keys():
            word_dict[word] = word_dict[word] + 1
        else:
            word_dict[word] = 1

    print(f"{word_ls}\n")
    print("Bag of Words: ")
    for key in sorted(word_dict.keys()):
        print(f"{key} - {word_dict[word]}")

main()
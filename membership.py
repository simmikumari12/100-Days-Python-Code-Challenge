# Write a program that determines whether a given character is a vowel, consonant, digit, or punctuation.
# programmed according to the rubrics given in the class
def main():
    character = input("Please enter a character: ").lower()

    punctuation_list = [",", ";", ".", "?", "!"]
    digits_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    vowels_list = ["a", "e", "i", "o", "u"]

    # Not an ideal way of checking
    if character in punctuation_list:
        is_character = "punctuation"
    elif character in digits_list:
        is_character = "digit"
    elif character in vowels_list:
        is_character = "vowel"
    else:
        is_character = "consonent"

    print(f"The {character} is a {is_character}")

if __name__ == "__main__":
    main()

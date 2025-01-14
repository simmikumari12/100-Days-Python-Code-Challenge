#create a program to display questions to the user like KBC.
import sys
def main():
    print("\nIn 2022, which team became the first to score more than 500 runs on the first day of Test Match?\n")
    option_row_one = ["A:India", "B:Australlia"]
    option_row_two = ["C:New Zealand", "D:England"]

    questions = ["1: In 2022, which team became the first to score more than 500 runs on the first day of Test Match?",
                "2: Which of the following countries is the world's largest producer of saffron?",
                "3: Which god is also known as ‘Gauri Nandan’?",
                "4: What does not grow on tree according to a popular Hindi saying?",
                "5: Which city is known as the Pink City of India?",
                "6: Who wrote India's National Anthem?",
                "7: How many major religions are there in India?",
                "8: When is the National Hindi Diwas celebrated?",
                "9: Which country is the largest producer of coffee in the world?",
                "10: Where is India Gate located?",
                ]
    for question in questions:
        print(question)
        if answer is True:
            continue
        else:
            break
            sys.exit()

    for option in option_row_one:
        print(option.center(40), end=" ")
    print("\n")
    for option in option_row_two:
        print(option.center(40), end=" ")
    print("\n")


if __name__ == "__main__":
    main()
#create a program to display questions to the user like KBC.
def main():
    print("\nIn 2022, which team became the first to score more than 500 runs on the first day of Test Match?\n")
    option_row_one = ["A:India", "B:Australlia"]
    option_row_two = ["C:New Zealand", "D:England"]
    for option in option_row_one:
        print(option.center(40), end=" ")
    print("\n")
    for option in option_row_two:
        print(option.center(40), end=" ")
    print("\n")


if __name__ == "__main__":
    main()
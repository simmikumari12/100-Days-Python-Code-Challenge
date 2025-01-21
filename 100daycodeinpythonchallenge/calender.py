def my_input():
    month = input("Please Enter the month: ").title()
    day = input("Please Enter the day: ")
    classifier(month, day)

def classifier(my_month, my_day):
    month = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }
    if 3<= month[my_month] <=6:
        print("between March and June")

    print(month[my_month])
    print(type(month[my_month]))

my_input()
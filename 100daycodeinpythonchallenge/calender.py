def my_input():
    month = input("Please Enter the month: ").title()
    day = input("Please Enter the day: ")
    classifier(month, day)

def classifier(my_month, d):
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
    m = month[my_month]
    
    if m == 3:
        if d > 20:
            print(f"{my_month} {d} is  summer in the southern hemisphere.")
    if m == 6 :
        if d < 20:
            print(f"{my_month} {d} is  summer in the southern hemisphere.")

    if 3 < m < 6: 
        print(f"{my_month} {d} is  summer in the southern hemisphere.")

    print(month[my_month])
    print(type(month[my_month]))

my_input()
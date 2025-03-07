def main():
    month = input("Please Enter the month: ").title()
    day = int(input("Please Enter the day: "))
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
            print(f"{my_month} {d} is autumn in the southern hemisphere.")
        else:
            print(f"{my_month} {d} is summer in the southern hemisphere.")

    if m == 6 :
        if d < 20:
            print(f"{my_month} {d} is autumn in the southern hemisphere.")
        else:
            print(f"{my_month} {d} is winter in the southern hemisphere.")

    if m == 9:
        if d > 21:
            print(f"{my_month} {d} is spring in the southern hemisphere.")
        else:
            print(f"{my_month} {d} is winter in the southern hemisphere.")        
  
    if m == 12 :
        if d < 20:
            print(f"{my_month} {d} is  spring in the southern hemisphere.")
        else:
            print(f"{my_month} {d} is  summer in the southern hemisphere.")

    if 3 < m < 6: 
        print(f"{my_month} {d} is autumn in the southern hemisphere.")

    if 6 < m < 9: 
        print(f"{my_month} {d} is winter in the southern hemisphere.")

    if 9 < m < 12: 
        print(f"{my_month} {d} is spring in the southern hemisphere.")
    
    if 1 <= m < 3: 
        print(f"{my_month} {d} is summer in the southern hemisphere.")

if __name__ == "__main__":
    main()
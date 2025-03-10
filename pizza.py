import sys
import tabulate
import csv

def main():
    valid_input()
    print(my_table(sys.argv[1]))

def valid_input():
    l = len(sys.argv)
    if l > 2:
        sys.exit("Too many command line arguments")
    if l < 2:
        sys.exit("Too Few Command Line Arguments")

    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file.")

    try:
        with open(sys.argv[1], "r") as f:
            ...
    except FileNotFoundError:
        sys.exit("File does not exist.")

def my_table(my_file):
    menu = []
    with open(my_file, "r") as file:
        items = csv.reader(file)

        for item in items:
            menu.append(item)
       
    return tabulate.tabulate(menu[1:], menu[0], tablefmt = "grid")

if __name__ == "__main__":
    main()
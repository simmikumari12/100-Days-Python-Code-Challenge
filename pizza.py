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
    ...
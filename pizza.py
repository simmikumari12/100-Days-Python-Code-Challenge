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

    



def my_table(my_file):
    ...
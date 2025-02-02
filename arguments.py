import sys
from functools import reduce

def main():
    arguments_ls = []
    for argv in sys.argv[1:]:
        try:
            arguments_ls.append(float(argv))
        except ValueError:
            print("Invalid Input!")
            sys.exit()

    print(f"{reduce(lambda x, y: x * y,arguments_ls, 1 ):0.3}")

if __name__ == "__main__":
    main()


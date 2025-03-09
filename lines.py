import sys

def main():

    l = len(sys.argv)
    if l > 2:
        sys.exit("Too many command line arguments")
    elif l < 2:
        sys.exit("Too few command line arguments")
    
    if not (sys.argv[1].endswith(".py")):
        sys.exit("Not a valid python file.")

    
    print(num_lines(sys.argv[1]))


def num_lines(my_file):
    ...


if __name__ == "__main__":
    main()
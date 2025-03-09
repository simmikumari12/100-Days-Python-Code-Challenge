import sys

def main():
    valid_input()
    print(num_lines(sys.argv[1]))

def valid_input():

    l = len(sys.argv)
    if l > 2:
        sys.exit("Too many command line arguments")
    elif l < 2:
        sys.exit("Too few command line arguments")
    
    if not (sys.argv[1].endswith(".py")):
        sys.exit("Not a valid python file.")

    try:
        with open(sys.argv[1], "r") as f:
            ...
    except FileNotFoundError:
        sys.exit("File does not exist.")
    
    

def num_lines(my_file):
    count = 0
    with open(my_file, "r") as f:
        for line in f:
            if (not (line.startswith("#"))) and (len(line.strip()) != 0):
                count = count + 1
    return count



if __name__ == "__main__":
    main()
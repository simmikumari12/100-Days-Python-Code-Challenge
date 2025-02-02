from functools import reduce

def main():
    write_in_file()
    read_from_file()

def write_in_file():
    file = open("numbers.txt", "w")
    nums_to_write = input("Give numbers to write: ")
    file.write(nums_to_write)
    file.close()

def read_from_file():
    file = open("numbers.txt", "r")
    for nums in file:
        a_list = nums.split(" ")
    try:
        print(reduce(lambda x, y: float(x) * float(y), a_list, 1))
    except:
        print("Invalid Input!")

    file.close()

if __name__ == "__main__":
    main()
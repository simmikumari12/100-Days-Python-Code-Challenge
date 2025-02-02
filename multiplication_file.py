from functools import reduce

def main():
    write_to_file()
    read_from_file()

def write_to_file():
    file1 = open("numbers.txt", "w")
    nums_to_write = input("Give numbers to write: ")
    file1.write(nums_to_write)
    file1.close()

def read_from_file():
    file2 = open("numbers.txt", "r")
    for nums in file2:
        a_list = nums.split(" ") # could have used file.writelines
    try:
        value = reduce(lambda x, y: float(x) * float(y), a_list, 1)
        print(value)
        
    except:
        print("Invalid Input!")
        
    file2.close()

    file3 = open("numbers.txt", "a")
    file3.write(f" = {value}")
    file3.close()

if __name__ == "__main__":
    main()
from functools import reduce
def main():
    while True:
        try:
            n = int(input("n = "))
            break
        except ValueError:
            print("Invalid input!")
        except TypeError:
            print("Please Enter a positive number!")



    print(f"Sum of first {n} numbers = {reduce(lambda x, y: x + y, range(n+1))}")

if __name__ == "__main__":
    main()

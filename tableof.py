def main():
    while True:
        try:
            num = int(input("Write table of: "))
            break
        except ValueError:
            print("Invalid Input")
            

    for i in range(1, 11):
        print(f"{num} * {i} = {i * num}")

if __name__ == "__main__":
    main()
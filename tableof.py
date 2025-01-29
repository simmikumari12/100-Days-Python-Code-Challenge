def main():

    while True:
        try:
            num = int(input("\nTable of "))
            break
        except ValueError:
            print("Invalid Input")
            
    for i in range(1, 11):
        print(f"{num} * {i} = {i * num}")
    print("\n")

if __name__ == "__main__":
    main()
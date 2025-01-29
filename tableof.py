def main():
    num = int(input("Write table of: "))

    for i, val in enumerate(range(10), start = 1):
        print(f"{num} * {i} = {i* num}")

if __name__ == "__main__":
    main()
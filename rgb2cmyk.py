def main():
    print("RGB To CMYK Converter")
    red = int(input("Enter the Red Color Value (enter quit or q to quit): "))
    green = int(input("Enter the Green Color Value: "))
    blue = int(input("Enter the Blue Color Value: "))
    print("CMYK Values")
    print(RGB_to_CMYK(red, green, blue))

def RGB_to_CMYK():
    pass

if __name__ == "__main__":
    main()
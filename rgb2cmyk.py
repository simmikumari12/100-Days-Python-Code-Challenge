import sys

def main():
    while True:
        print("RGB To CMYK Converter")
        red = input("Enter the Red Color Value (enter quit or q to quit): ")
        if red == "quit" or red == "q":
            sys.exit()

        green = int(input("Enter the Green Color Value: "))
        blue = int(input("Enter the Blue Color Value: "))
        print("CMYK Values")
        my_dict = RGB_to_CMYK(int(red), green, blue)
        for key in my_dict:
            print(f"{key}: {my_dict[key]}")

        

def RGB_to_CMYK(r, g, b):
    r1 = r/255
    g1 = g/255
    b1 = b/255

    k1 = 1 - max(r1, g1, b1)

    c = round(((1 - r1 - k1) * 100) / (1 - k1))
    m = round(((1 - g1 - k1) * 100) / (1 - k1))
    y = round(((1 - b1 - k1) * 100) / (1 - k1))
    k = round(k1 * 100)

    cmyk = {
        "Cyan": c,
        "Magenta": m,
        "Yellow": y,
        "Key (Black)": k
    }

    return cmyk



if __name__ == "__main__":
    main()
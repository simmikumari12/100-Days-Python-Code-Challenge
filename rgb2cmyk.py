def main():
    print("RGB To CMYK Converter")
    red = int(input("Enter the Red Color Value (enter quit or q to quit): "))
    green = int(input("Enter the Green Color Value: "))
    blue = int(input("Enter the Blue Color Value: "))
    print("CMYK Values")
    print(RGB_to_CMYK(red, green, blue))

def RGB_to_CMYK(r, g, b):
    r1 = r/255
    g1 = g/255
    b1 = b/255

    k1 = 1 - max(r1, g1, b1)

    c = round(((1 - r1 - k1) * 100) / (1 - k1))
    m = ((1 - g1 - k1) * 100) / (1 - k1)
    y = ((1 - b1 - k1) * 100) / (1 - k1)
    k = k1 * 100

    cmyk = {
        "C": c,
        "M": m,
        "Y": y,
        "K": k
    }

    return cmyk



if __name__ == "__main__":
    main()
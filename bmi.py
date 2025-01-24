def main():
    w = float(input("Enter Weight in kg: "))
    h = float(input("Enter Height in meter: "))
    print(calc_BMI(w, h))

def calc_BMI(weight, height):
    return f"The BMI for this person is {((weight)/(height * 2)):0.3f}"

if __name__ == "__main__":
    main()

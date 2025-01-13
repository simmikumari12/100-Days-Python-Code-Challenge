def feet_to_steps(num_feet):
    num_steps = int(num_feet * 2.5)
    return num_steps
def main():
    num_feet = int(input("Please enter the distance travelled in feets: "))
    print(feet_to_steps(num_feet),"steps")

if __name__ == "__main__":
    main()
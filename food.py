menu = {
    "Hot Dog": 1.5,
    "Slice of Pizza": 1.99,
    "Whole Pizza":9.95,
    "Soft Drink": .59
}

num_dog = float(input("Please enter the number of Hot Dogs: "))
num_slice_pizza = float(input("Please enter the number of Pizza Slices: "))
num_whole_pizza = float(input("Please enter the number of Whole Pizzas: "))
num_drink = float(input("Please enter the number of Soft Drinks: "))

total = num_dog * menu["Hot Dog"] + num_slice_pizza * menu["Slice of Pizza"] + num_whole_pizza * menu["Whole Pizza"] + num_drink * menu["Soft Drink"]
print(f"The total cost of the order is {total:0.2f}")

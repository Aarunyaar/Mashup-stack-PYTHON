fruits = ["Apple", "Banana", "Mango"]
vegetables = ["Carrot", "Potato", "Tomato"]
beverages = ["Juice", "Soda", "Water"]

fruits.append("Orange")

vegetables.insert(1, "Onion")

beverages.pop()

inventory = [fruits, vegetables, beverages]

print("First two fruits:", fruits[:2])

print("Last vegetable:", vegetables[-1])

fruit_lengths = [len(item) for item in fruits]
print("Length of each fruit name:", fruit_lengths)

is_water_present = "Water" in beverages
print("Is 'Water' in beverages?", is_water_present)

first_items_tuple = (fruits[0], vegetables[0], beverages[0])
print("Tuple of first items:", first_items_tuple)

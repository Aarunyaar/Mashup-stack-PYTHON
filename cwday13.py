# Ask the user to enter a new item
item = input("Enter the name of the new stationery item: ")

filename = "items.txt"

# Try to open the file in append mode (creates the file if it does not exist)
with open(filename, "a") as file:
    file.write(item + "\n")

# Display the full list of items
print("\nCurrent list of stationery items:")
with open(filename, "r") as file:
    for line in file:
        print("- " + line.strip())

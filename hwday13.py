filename = "students.txt"

try:
    with open(filename, "r") as file:
        existing_names = file.read()
        if existing_names.strip():
            print("Existing student names:")
            print(existing_names)
        else:
            print("The file exists but is empty.")
except FileNotFoundError:
    print("No existing student file found. A new one will be created.")

count = int(input("\nHow many student names do you want to add? "))

with open(filename, "a") as file:
    for i in range(count):
        name = input(f"Enter name {i + 1}: ")
        file.write(name + "\n")

print("\nUpdated list of all student names:")
with open(filename, "r") as file:
    for line in file:
        print(line.strip())

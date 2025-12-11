grocery_list = ["milk", "bread", "eggs"]

def add_item(item):
    grocery_list.append(item)
    print(f'"{item}" added to list.')

def remove_last_item():
    if grocery_list:
        removed = grocery_list.pop()
        print(f'"{removed}" removed from list.')
    else:
        print("The list is already empty!")

display_item = lambda item: print(f"Item: {item}")

def count_characters(items):
    if not items:      
        return 0
    return len(items[0]) + count_characters(items[1:])   


print("Initial List:")
for item in grocery_list:
    display_item(item)

add_item("butter")
remove_last_item()

print("\nUpdated List:")
for item in grocery_list:
    display_item(item)

print("\nTotal characters:", count_characters(grocery_list))

inventory=[]

def add_item(item):
    inventory.append(item)

def count_items(items,index=0):
    if not items:
        return 0
    return 1+ count_items(items[1:])
show_item = lambda item: print(f"Item in Stock: {item}")


add_item("dog food")
add_item("cat toy")
add_item("bird cage")
add_item("fish tank")
print ("Items in the inventory list")
for x in inventory:
    show_item(x)
total = count_items(inventory)
print("\nTotal items in stock:", total)
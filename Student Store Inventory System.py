# Welcome message
print("Student Store Inventory System")
print("Welcome to the Student Store Inventory System!")

# Store information
store_name = input("Enter the name of the store: ")
owner_name = input("Enter the name of the store owner: ")
number_of_items = int(input("Enter the number of items in the store: "))

# Inventory list
inventory = []

# Collect item details
for i in range(number_of_items):
    item_name = input(f"Enter the name of item {i + 1}: ")
    item_price = float(input(f"Enter the price of {item_name}: $"))

    inventory.append((item_name, item_price))

# Display inventory
print("\nInventory List")
for item in inventory:
    print(f"{item[0]} - ${item[1]:.2f}")

# Check stock
item_to_check = input("\nEnter item to check stock: ")

in_stock = any(
    item[0].lower() == item_to_check.lower()
    for item in inventory
)

if in_stock:
    print(f"{item_to_check} is in stock.")
else:
    print(f"{item_to_check} is not in stock.")
"""
Build a system that prints invoice lines with consistent spacing. 
Each line must align the item name left and the price right, padded to a fixed width.
"""
item_name = input("Enter the item name: ")
price = float(input("Enter the price of the item: "))
fixed_width = 30  # Total width for the line
formatted_line = f"{item_name:<{fixed_width - len(str(price))}}{price:>10.2f}"
print(formatted_line)
"""
A warehouse system checks if items are the same object in memory (identity) vs just equal in value (equality). 
Explore the difference between == and 'is'.

"""
stock_a = [10, 20, 30]
stock_b = [10, 20, 30]
stock_c = stock_a

print("stock_a == stock_b:", stock_a == stock_b)  # True
print("stock_a is stock_b:", stock_a is stock_b)  # False
print("stock_a is stock_c:", stock_a is stock_c)  # True
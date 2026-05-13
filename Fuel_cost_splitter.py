"""
Four friends split fuel cost. N750/litre, 40 litres. 
One friend can only pay half a share. 
Calculate each person's amount.

"""

price_per_litre = int(input("Enter the price per litre of fuel: "))
litres = int(input("Enter the number of litres: "))
friends = int(input("Enter the number of friends sharing the cost: "))

total_cost = price_per_litre * litres
half_payer_share = total_cost / (friends + 0.5)  # Half payer counts as 0.5
full_payer_share = half_payer_share * 2  # Full payers pay double   
print(f"Total fuel cost: N{total_cost}")
print(f"Each full payer pays: N{full_payer_share}") 
print(f"The half payer pays: N{half_payer_share}")

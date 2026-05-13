"""
A user has N500 airtime. 
Calls cost N15 per minute. 
Calculate how many full minutes they can call and what balance is left over.

"""
balance = 500
cost_per_minute = 11
minutes = float(balance) // float(cost_per_minute)
remaining_balance = float(balance) % float(cost_per_minute)
print(f"You can call for {minutes} minutes and your remaining balance is N{remaining_balance}.")
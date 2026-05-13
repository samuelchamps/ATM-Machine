"""
An ATM checks if the user has enough balance, if the amount is a multiple of 500, and if it does not exceed the daily limit of N100,000.
"""

balance = int(1000000)
withdrawal_amount = float(input("Enter the amount to withdraw: "))
daily_limit = 100000

if withdrawal_amount > balance:
    print(f"Insufficient balance. Your current balance is N{balance:.2f}.   ")

elif withdrawal_amount > daily_limit:
    print(f"Withdrawal amount exceeds the daily limit of N{daily_limit:.2f}.")  

elif withdrawal_amount % 500 != 0:
    print("Withdrawal amount must be a multiple of N500.")
else:
    balance -= withdrawal_amount
    print(f"Withdrawal successful. Your new balance is N{balance:.2f}.")

# Annotated Budget Script
"""
Write a script that calculates a monthly budget.
Add a comment above every line explaining what it does.
This builds the habit of writing readable code.
"""
monthly_income = 5000  # This variable stores the monthly income
rent = 1500  # This variable stores the monthly rent expense
utilities = 300  # This variable stores the monthly utilities expense
groceries = 400  # This variable stores the monthly groceries expense
transportation = 200  # This variable stores the monthly transportation expense
entertainment = 150  # This variable stores the monthly entertainment expense
savings = 500  # This variable stores the monthly savings
total_expenses = rent + utilities + groceries + transportation + entertainment  # This variable calculates the total monthly expenses
remaining_budget = monthly_income - total_expenses - savings  # This variable calculates the remaining budget
print(f"Monthly Income: #{monthly_income}")  # This line prints the monthly income
print(f"Total Expenses: #{total_expenses}")  # This line prints the total expenses
print(f"Savings: #{savings}")  # This line prints the savings
print(f"Remaining Budget: #{remaining_budget}")  # This line prints the remaining budget
"""
A form collects age as text (because input() always returns a string). 
Cast it to an integer, then calculate what year the person was born.

"""
age = int(input("Enter your age: "))
current_year = 2023
birth_year = current_year - age
print(f"You were born in {birth_year}.")
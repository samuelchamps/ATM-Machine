"""
A registration system auto-generates usernames. 
Strip whitespace, lowercase both names, then join them with an underscore.

"""
first_name = input("Enter your first name: ").strip().lower()
last_name = input("Enter your last name: ").strip().lower()
username = first_name + "_" + last_name
print(f"Your username is: {username}")
print(f"Your full name is: {first_name} {last_name}")
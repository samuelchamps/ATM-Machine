"""
A site checks if a user is 18+ and their password is 8+ characters. 
Print True/False for each check and a combined 'Can register' result.

"""
age = int(input("Enter your age: "))
password = input("Enter your password: ")

is_adult = age >= 18
is_valid_password = len(password) >= 8
can_register = is_adult and is_valid_password

print(f"Is adult: {is_adult}")
print(f"Is valid password: {is_valid_password}")
print(f"Can register: {can_register}")
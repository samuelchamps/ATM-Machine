"""
Given an email address, extract just the domain name (the part after @). 
This is a real task in backend validation systems.

"""

email = input("Enter your email address: ")
domain = email.split("@")[1]
provider = domain.split(".")[0]
print(f"The domain of the email address is: {domain}")
print(f"The email provider is: {provider}")
# ## List of servers
# servers = [ "printserver", "fileserver", "webserver", "dbserver", "mailserver" ]
# print(servers)

# ## Adding a new server
# servers.append("backupserver")
# print(servers)

# ## Removing a server a server by name
# servers.remove("dbserver")
# print(servers)

# ## Removing a server by index
# del servers[2]
# print(servers)

# ## Extending the server list with multiple new servers
# new_servers = ["proxyserver", "vpnserver", "authserver"]
# servers.extend(new_servers)
# print(servers)

# ## looping through the server list
# for server in servers:
#     print(server.upper())

# ## list comprehension to create a new list of server names that contain 'i'
# i_servers = [server for server in servers if 'i' in server]
# print(i_servers)

# servers = ["web1", "db1", "web2", "cache1", "web3"]
# ## create a list of only servers that start with 'web'
# web_servers = [server for server in servers if server.startswith('web')]
# print(web_servers)

# ## Mini project: Using  tuples

# services = ("Ec2", "S3", "Lambda", "DynamoDB", "RDS")
# regions = ("us-east-1", "us-west-2", "eu-central-1")

# for service in services:
#     for region in regions:
#         print(f"Deploying {service} in {region}")


# servers = (
#     ("web1", "running", 80),
#     ("web2", "stopped", 80),
#     ("db1", "running", 3306),
#     ("cache1", "running", 6379),
# )
# for server in servers:
#     name, status, port = server
#     print(f"Server: {name} is {status} on port {port}")

# # Covert your weight in pounds
# user_weight = input("What is your weight in pounds? ")
# weight_kg = float(user_weight) * 0.453592
# print(f"Your weight in kilograms is: {weight_kg:.2f} kg")

# username = input("Enter your username: ")
# if len(username) < 3:
#     print("Username must be at least 3 characters long.")
# elif len(username) > 50:
#     print("Username must be no more than 50 characters long.")
# else:
#     print("Username looks good!")

# ## A car game
# ## Type help to see the commands
# ## start - to start the car
# ## stop - to stop the car
# ## quit - to exit the game

# user_input = input("> ").lower()
# while user_input != "quit":
#     if user_input == "start":
#         print("Car started... Ready to go!")
#         break
#     elif user_input == "stop":
#         print("Car stopped.")
#         break
#     elif user_input == "help":
#         print("start - to start the car")
#         print("stop - to stop the car")
#         print("quit - to exit the game")
#         break
#     else:
#         print("I don't understand that command.")
# ## To calculate the number of shopping cart items
# cart_items = []
# while True:
#     item = input("Add an item to the cart (or type 'done' to finish): ")
#     if item.lower() == 'done':
#         break
#     cart_items.append(item)
# print(f"You have {len(cart_items)} items in your cart.")
# print("Thank you for shopping with us!")


## How to find the largest number in a list
numbers = [45, 22, 89, 12, 67, 34, 90, 11]
largest_number = numbers[0]
for number in numbers:
    if number > largest_number:
        largest_number = number
print(f"The largest number is: {largest_number}")

## remove duplicates from a list
numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3]
unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)
print(f"Unique numbers: {unique_numbers}")

## function to greet a user
def greet_user(name):
    print(f"Hello, {name}! Welcome aboard.")
greet_user("Alice")

## function to add two numbers
def add_numbers(a, b):
    return a + b
result = add_numbers(5, 7)
print(f"The sum is: {result}")

## function for a grade calculator
try:
    def student_score(score):
        if score >= 70 and score <= 100:
            return 'A'
        elif score >= 60 and score < 70:
            return 'B'
        elif score >= 50 and score < 60:
            return 'C'
        elif score >= 40 and score < 50:
            return 'D'
        else:
            return 'F'
    student_score = int(input("Enter the student's score (0-100): "))
    grade = student_score(student_score)
    print(f"The grade for score {student_score} is: {grade}")
except Exception as e:
    print(f"An error occurred: {e}")
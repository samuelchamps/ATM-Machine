"""
Every API returns an HTTP status code.
Use Python's match statement to handle different response codes.
"""

# Function
def handle_response(status_code):

    match status_code:

        case 200:
            return "OK: The request was successful."

        case 201:
            return "Created: The resource was successfully created."

        case 400:
            return "Bad Request: Invalid syntax."

        case 401:
            return "Unauthorized: Authentication is required."

        case 403:
            return "Forbidden: Access denied."

        case 404:
            return "Not Found: Resource not found."

        case 500:
            return "Internal Server Error."

        case _:
            return f"Unexpected status code: {status_code}"


# Main program loop
while True:

    user_input = int(
        input("\nEnter an HTTP status code (or 0 to exit): ")
    )

    # Exit condition
    if user_input == 0:
        print("Program ended.")
        break

    # Call function
    print(f"{user_input}: {handle_response(user_input)}")
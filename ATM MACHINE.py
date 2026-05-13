"""
Simple ATM Machine
"""

# Welcome message
print("Welcome to the ATM Machine!")

# Starting balance
show_balance = 1000.00

while True:

    # Ask for PIN
    pin = int(input("\nPlease enter your 4-digit PIN: "))

    # Check PIN
    if pin == 1234:

        print("\nPIN accepted.")

        # ATM Menu
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        # User chooses option
        option = input("Choose an option: ")

        # Check Balance
        if option == "1":
            print(f"\nYour current balance is: ${show_balance:.2f}")

        # Deposit
        elif option == "2":
            deposit_amount = float(
                input("Enter amount to deposit: $")
            )

            show_balance += deposit_amount

            print(
                f"Deposit successful. New balance: ${show_balance:.2f}"
            )

        # Withdraw
        elif option == "3":

            withdrawal_amount = float(
                input("Enter withdrawal amount: $")
            )

            # Check for sufficient funds
            if withdrawal_amount > show_balance:
                print("Insufficient funds.")

            else:
                show_balance -= withdrawal_amount

                print(
                    f"Withdrawal successful. New balance: ${show_balance:.2f}"
                )

        # Exit
        elif option == "4":
            print("Thank you for using the ATM Machine.")
            break

        # Invalid menu option
        else:
            print("Invalid option selected.")

    # Wrong PIN
    else:
        print("Invalid PIN. Please try again.")
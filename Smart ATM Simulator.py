accounts_data = {
    "123456789": {"name": "ali", "pin": 123, "balance": 1000.0},
    "987654321": {"name": "babar", "pin": 123, "balance": 500.0},
    "111222333": {"name": "umer", "pin": 123, "balance": 750.0},
    "234567890": {"name": "sara", "pin": 123, "balance": 1200.0},
    "345678901": {"name": "nida", "pin": 123, "balance": 300.0},
    "456789012": {"name": "ahmed", "pin": 123, "balance": 800.0},
    "567890123": {"name": "fatima", "pin": 123, "balance": 950.0},
    "678901234": {"name": "osman", "pin": 123, "balance": 600.0},
    "789012345": {"name": "zain", "pin": 123, "balance": 400.0},

}

def main():
    print("Welcome to the Python ATM!")
    print("Please enter your account number:")
    account_number = input()
    print("Please enter your PIN:")
    pin = int(input())

    if accounts_data[account_number]["pin"] != pin:
        print("Incorrect PIN. Please try again.")
        return


    if account_number in accounts_data and accounts_data[account_number]["pin"] == pin:
        print("Account login Successful!")
        account = accounts_data[account_number]
        account['balance'] = float(account["balance"])
        print(f"Hello {account['name']}! Your current balance is: ${account['balance']}")
        
        while True:
            print("\nWhat would you like to do?")
            print("1. Withdraw Money")
            print("2. Deposit Money")
            print("3. Check Balance")
            print("4. Exit")
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                amount = float(input("Enter amount to withdraw: $"))
                if amount <= account["balance"]:
                    account["balance"] -= amount
                    print(f"Withdrawal successful! New balance: ${account['balance']}")
                else:
                    print("Insufficient funds!")

            elif choice == '2':
                amount = float(input("Enter amount to deposit: $"))
                account['balance'] += amount
                print(f"Deposit successful! New balance: ${account['balance']}")

            elif choice == '3':
                print(f"Your current balance is: ${account['balance']}")

            elif choice == '4':
                print("Thank you for using the Python Smart ATM Simulator! Goodbye!")
                break

            else:
                print("Invalid choice, please try again.")
    else:
        print("Account number not found. Please try again.")

if __name__ == "__main__":
    main()
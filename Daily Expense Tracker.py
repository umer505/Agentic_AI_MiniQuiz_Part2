expense_count= {
    "13-06-2025" : [
        {
        "category": "food",
        "amount": 15.50,
    },
    {
        "category": "transport",
        "amount": 5.00,
    },
    {
        "category": "entertainment",
        "amount": 20.00,
    },
    {
        "category": "utilities",
        "amount": 30.00,
    },
    ],
    "14-06-2025" : [
         {
        "category": "groceries",
        "amount": 25.00,
    },
    {
        "category": "health",
        "amount": 10.00
    },
    {
        "category": "clothing",
        "amount": 40.00
    },
    {
        "category": "home accessories",
        "amount": 60.00
    },
    ]
}


def calculate_total_expense(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total

def calculate_category_expenses(expenses):
    category_expenses = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        if category in category_expenses:
            category_expenses[category] += amount
        else:
            category_expenses[category] = amount
    return category_expenses

def display_expenses(expenses):
    print("Date: 13-06-2025")
    print("Expenses:")
    for expense in expenses:
        print(f"Category: {expense['category']}, Amount: ${expense['amount']:.2f}")
    print(f"Total Expense: ${calculate_total_expense(expenses):.2f}")
    
    category_expenses = calculate_category_expenses(expenses)
    print("\nCategory-wise Expenses:")
    for category, amount in category_expenses.items():
        print(f"{category.capitalize()}: ${amount:.2f}")

def main():

    print("Daily Expense Tracker")
    
    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View by Category")
        print("4. View by Date")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            date = input("Enter the date (dd-mm-yyyy): ")
            category = input("Enter the category: ")
            amount = float(input("Enter the amount: "))
            
            if date not in expense_count:
                expense_count[date] = []
            expense_count[date].append({"category": category, "amount": amount})
            print("Expense added successfully!")

        elif choice == '2':
            for date, expenses in expense_count.items():
                print(f"\nDate: {date}")
                display_expenses(expenses)
        
        elif choice == '3':
            category = input("Enter the category: ")
            found = False
            for date, expenses in expense_count.items():
                category_expenses = [expense for expense in expenses if expense["category"].lower() == category.lower()]
                if category_expenses:
                    found = True
                    print(f"\nDate: {date}")
                    display_expenses(category_expenses)
            if not found:
                print(f"No expenses found for category '{category}'.")
        
        elif choice == '4':
            date = input("Enter the date (dd-mm-yyyy): ")
            if date in expense_count:
                print(f"\nExpenses for {date}:")
                display_expenses(expense_count[date])
            else:
                print(f"No expenses found for date '{date}'.")
        
        elif choice == '5':
            print("Exiting the Daily Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
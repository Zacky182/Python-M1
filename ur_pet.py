from tabulate import tabulate
import datetime

def login():
    # Dummy user credentials for demonstration purposes
    valid_credentials = {"user123": "pass123"}

    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in valid_credentials and valid_credentials[username] == password:
            print("Login successful!")
            return username
        else:
            print("Invalid username or password. Please try again.")

transactions = []

def display_menu():
    print(''''  
                    Hello!
             Welcome to Ur.PET
        Your Personal Expense Tracking
           
    1. Target Expense for Today
    2. Add Transaction
    3. Remove Transaction
    4. Update Transaction
    5. Summarize Expenses
    6. Exit     
''')  

    # Calculate and display current target expense remaining
    if 'target_expense' in globals():
        total_expense = sum(transaction[3] for transaction in transactions)
        target_remaining = target_expense - total_expense
        print("Current Target Expense Remaining $:", target_remaining)
    else:
        print("Please set target expense for today first.")

def set_target_expense():
    global target_expense
    if 'target_expense' in globals():
        print("Target expense has already been set. It can only be entered once.")
        return

    print("Only once can you set a target. \nIf you're not convinced with the target for today, you can choose \"No\" to go back to the menu.")
    
    while True:
        confirm = input("Are you sure you want to set the target expense? (Yes/No): ")
        if confirm.lower() == 'no':
            print("Target expense setting cancelled.")
            return
        elif confirm.lower() == 'yes':
            break
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")
            
    while True:
        user_input = input("Enter target expense for today $: ")
        try:
            target_expense = float(user_input)
            if target_expense < 0:
                print("Invalid input. Please enter a non-negative number for the target expense.")
            else:
                print("Target expense  set successfully!")
                return
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def validate_date_format(date):
    try:
        # Attempt to parse the date string
        datetime.datetime.strptime(date, '%d-%m-%Y')
        return True
    except ValueError:
        # If parsing fails, return False
        return False

def add_transaction():
    while True:
        print("Add Transaction:\n")
        while True:
            date = input("Enter transaction date (DD-MM-YYYY): ")
            if not validate_date_format(date):
                print("Invalid date format. Please use DD-MM-YYYY format.")
            else:
                # Reformat the date to ensure leading zeros for days and months
                date_parts = date.split('-')
                date = '-'.join([part.zfill(2) for part in date_parts])
                break

        category = input("Enter transaction category: ")
        
        while True:
            try:
                amount = float(input("Enter transaction amount $: "))
                if amount < 0:
                    print("Invalid input. Please enter a non-negative number for the transaction amount.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number for the transaction amount.")

        details = input("Enter transaction details: ")

        # Automatically generate ID
        if transactions:
            new_id = transactions[-1][0] + 1
        else:
            new_id = 1

        transactions.append([new_id, date, category, amount, details])
        print("Transaction added successfully!")
        view_transactions()

        while True:
            choice = input("Will you add more transactions? (Yes/No): ")
            if choice.lower() == "yes":
                break
            elif choice.lower() == "no":
                return
            else:
                print("Invalid input. Please enter 'Yes' or 'No'.")

def remove_transaction():
    if not transactions:
        print("No transactions available to remove.")
        return
    
    while True:
        view_transactions()
        print("Remove Transaction\n")
        index_input = input("Enter ID of transaction to remove: ")
        if not index_input.isdigit():
            print("Invalid input. Please enter a valid ID number.")
            continue
        index_to_remove = int(index_input)
        if 0 < index_to_remove <= len(transactions):
            del transactions[index_to_remove - 1]
            print("Transaction removed successfully!")

            # Reassign IDs to transactions
            for i in range(len(transactions)):
                transactions[i][0] = i + 1
            view_transactions()
            
            while True:
                choice = input("Do you want to remove another transaction? (Yes/No): ")
                if choice.lower() == "yes":
                    break
                elif choice.lower() == "no":
                    return
                else:
                    print("Invalid input. Please enter 'Yes' or 'No'.")
            
        else:
            print("Invalid, please input valid transaction ID!")

def update_transaction():
    if not transactions:
        print("No transactions available to update.")
        return

    while True:
        view_transactions()
        print("Update Transaction\n")
        index_input = input("Enter ID of transaction to update: ")
        if not index_input.isdigit():
            print("Invalid input. Please enter a valid ID number.")
            continue
        index_to_update = int(index_input)
        if 0 < index_to_update <= len(transactions):
            print("Current transaction details:")
            print(transactions[index_to_update - 1])
            print("Enter new transaction details:")
            
            while True:
                date = input("Enter transaction date (DD-MM-YYYY): ")
                if not validate_date_format(date):
                    print("Invalid date format. Please use DD-MM-YYYY format.")
                else:
                    # Reformat the date to ensure leading zeros for days and months
                    date_parts = date.split('-')
                    date = '-'.join([part.zfill(2) for part in date_parts])
                    break

            category = input("Enter transaction category: ")
            
            while True:
                try:
                    amount = float(input("Enter transaction amount $: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number for the transaction amount.")

            details = input("Enter transaction details: ")

            transactions[index_to_update - 1] = [index_to_update, date, category, amount, details]
            view_transactions()
            print("Transaction updated successfully!")

            while True:
                choice = input("Do you want to update another transaction? (Yes/No): ")
                if choice.lower() == "yes":
                    break
                elif choice.lower() == "no":
                    return
                else:
                    print("Invalid input. Please enter 'Yes' or 'No'.")
        else:
            print("Invalid, please input valid transaction ID!")

def view_transactions():
    print("Transactions:\n")
    headers = ["ID", "Date", "Category", "Amount ($)", "Details"]
    data = [[transaction[0], transaction[1], transaction[2].upper(), transaction[3], transaction[4].upper()] for transaction in transactions]
    print(tabulate(data, headers=headers, tablefmt="rounded_grid"))

def summarize_expenses():
    if 'target_expense' not in globals():
        print("Please set target expense for today first.")
        return

    if not transactions:
        print("No transactions yet.")
        return

    print("\nExpense Tracking:\n")
    headers = ["ID", "Category", "Date", "Amount ($)", "Details"]
    data = [[transaction[0], transaction[2].upper(), transaction[1], transaction[3], transaction[4].upper()] for transaction in transactions]
    print(tabulate(data, headers=headers, tablefmt="rounded_grid"))

    total_expense = sum(transaction[3] for transaction in transactions)
    print("Target Set Today $: ", total_expense)
    print("\nTotal Expense for Today $:", total_expense)

    remaining = target_expense - total_expense
    if remaining > 0:
        print(f"Great! You are saving ${remaining:.2f} left.")
    elif remaining == 0:
        print("You've reached your target expense for today!")
    else:
        print(f"Be wise! You are over ${abs(remaining):.2f} than target!")

def main():
    # Login before accessing the menu
    username = login() 
    print(f"Welcome, {username}!\n")   
    while True:
        display_menu()
        choice = input("Please input menu number: ")

        if choice == '1':
            set_target_expense()

        elif choice == '2':
            add_transaction()

        elif choice == '3':
            remove_transaction()
        
        elif choice == '4':
            update_transaction()

        elif choice == '5':
            summarize_expenses()

        elif choice == '6':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
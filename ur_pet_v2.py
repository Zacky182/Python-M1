import csv
from tabulate import tabulate
import datetime

def login():
    # Dummy user credentials for demonstration purposes
    valid_credentials = {"1": "1"}

    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in valid_credentials and valid_credentials[username] == password:
            print("Login successful!")
            return username
        else:
            print("Invalid username or password. Please try again.")

def display_menu(target_expense=None):
    print('''  
                    Hello!
             Welcome to Ur.PET
        Your Personal Expense Tracking
           
    1. Target Expense for Today
    2. Add Transaction
    3. Remove Transaction
    4. Update Transaction
    5. Summarize Expenses
    6. View Transaction History
    7. Reset Transaction History
    8. Exit     
''')

    if target_expense is not None:
        total_expense = sum(transaction['amount'] for transaction in transactions)
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
        confirm = input("Are you sure you want to set the target expense? (Yes/No): ").lower()
        if confirm == 'no':
            print("Target expense setting cancelled.")
            return
        elif confirm == 'yes':
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
                print("Target expense set successfully!")
                return target_expense  # Return the updated target expense
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

def add_transaction(transactions):
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
        new_id = len(transactions) + 1

        # Create a dictionary representing the transaction
        transaction = {
            "id": new_id,
            "date": date,
            "category": category,
            "amount": amount,
            "details": details
        }

        transactions.append(transaction)
        print("Transaction added successfully!")
        view_transactions()

        while True:
            choice = input("Will you add more transactions? (Yes/No): ").lower()
            if choice == "yes":
                break
            elif choice == "no":
                return
            else:
                print("Invalid input. Please enter 'Yes' or 'No'.")

def remove_transaction(transactions):
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
                transactions[i]['id'] = i + 1
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

def update_transaction(transactions):
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

            # Update the transaction details in the list
            transactions[index_to_update - 1] = {
                "id": index_to_update,
                "date": date,
                "category": category,
                "amount": amount,
                "details": details
            }
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
    data = [[transaction['id'], transaction['date'], transaction['category'].upper(), transaction['amount'], transaction['details'].upper()] for transaction in transactions]
    print(tabulate(data, headers=headers, tablefmt="rounded_grid"))

def summarize_expenses(transactions):
    if 'target_expense' not in globals():
        print("Please set target expense for today first.")
        return

    if not transactions:
        print("No transactions yet.")
        return

    print("\nExpense Tracking:\n")
    headers = ["ID", "Category", "Date", "Amount ($)", "Details"]
    data = [[transaction['id'], transaction['category'].upper(), transaction['date'], transaction['amount'], transaction['details'].upper()] for transaction in transactions]
    print(tabulate(data, headers=headers, tablefmt="rounded_grid"))

    total_expense = sum(transaction['amount'] for transaction in transactions)
    print("Target Set Today $: ", total_expense)
    print("\nTotal Expense for Today $:", total_expense)

    remaining = target_expense - total_expense
    if remaining > 0:
        print(f"Great! You are saving ${remaining:.2f} left.")
    elif remaining == 0 :
        print("You've reached your target expense for today!")  
    else:
        print(f"Be wise! You are over ${abs(remaining):.2f} than target!")

def view_transaction_history():
    transactions = read_transaction_history()
    if transactions:
        print("\nTransaction History:\n")
        headers = ["ID", "Date", "Category", "Amount ($)", "Details"]
        data = [[transaction['ID'], transaction['Date'], transaction['Category'], transaction['Amount ($)'], transaction['Details']] for transaction in transactions]
        print(tabulate(data, headers=headers, tablefmt="rounded_grid"))
    else:
        print("\nNo transaction history available.")

def read_transaction_history():
    transactions = []
    try:
        with open('transaction_history.csv', 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                transactions.append(row)
    except FileNotFoundError:
        pass  # If the file doesn't exist yet, return an empty list
    return transactions

def write_transaction_history(transactions):
    fieldnames = ["ID", "Date", "Category", "Amount ($)", "Details"]
    try:
        # Read the existing transactions from the CSV file
        existing_transactions = read_transaction_history()

        # Find the maximum existing ID to determine the starting point for new IDs
        max_id = max(int(transaction["ID"]) for transaction in existing_transactions) if existing_transactions else 0

        with open('transaction_history.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # If the file is empty, write the header
            if file.tell() == 0:
                writer.writeheader()

            for transaction in transactions:
                # Increment the ID for each new transaction
                max_id += 1
                transaction["ID"] = max_id

                # Convert keys in transaction dictionary to match fieldnames
                row = {
                    "ID": transaction["ID"],
                    "Date": transaction["date"],
                    "Category": transaction["category"],
                    "Amount ($)": transaction["amount"],
                    "Details": transaction["details"]
                }
                writer.writerow(row)
    except FileNotFoundError:
        print("Error: transaction_history.csv file not found.")
    
def reset_transaction_history():
    while True:
        if not transactions:  # Check if there are no transaction history
            print("No transaction history available.")
            break  # Exit the loop if there is no transaction history
        
        confirm = input("Are you sure you want to reset all transaction history? (Yes/No): ").lower()
        if confirm == 'yes':
            # Clear the transactions list
            transactions.clear()
            # Clear the transaction history file
            open('transaction_history.csv', 'w').close()
            print("Transaction history has been reset.")
            break  # Exit the loop if the input is valid
        elif confirm == 'no':
            print("Reset cancelled.")
            break  # Exit the loop if the input is valid
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")

def main():
    global transactions
    transactions = []
    target_expense = None  # Initialize target expense to None

    # Login before accessing the menu
    username = login() 
    print(f"Welcome, {username}!\n")   

    while True:
        display_menu(target_expense)  # Pass target_expense to the display_menu function

        choice = input("Please input menu number: ")

        if choice == '1':
            target_expense = set_target_expense()  # Capture the updated target expense

        elif choice == '2':
            add_transaction(transactions)  # Pass transactions list

        elif choice == '3':
            remove_transaction(transactions)  # Pass transactions list
        
        elif choice == '4':
            update_transaction(transactions)  # Pass transactions list

        elif choice == '5':
            summarize_expenses(transactions)  # Pass transactions list

        elif choice == '6':
            view_transaction_history()

        elif choice == '7':
            reset_transaction_history()

        elif choice == '8':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")

    # Write transaction history to CSV file before exiting
    write_transaction_history(transactions)

    print("Thank you for using the program!")

if __name__ == "__main__":
    main()

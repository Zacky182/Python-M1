from tabulate import tabulate

menu = {
    "Foods": {
        1: {"name": "Butter Croissant", "stock": 10, "price": 5.00},
        2: {"name": "Cheesy Garlic Croissant", "stock": 15, "price": 6.00},
        3: {"name": "Scrambled Eggs", "stock": 20, "price": 7.00},
        4: {"name": "Chicken Nuggets (8 Pcs)", "stock": 15, "price": 8.00},
        5: {"name": "Waffles (with Maple Syrup)", "stock": 15, "price": 10.00},
        6: {"name": "Blueberry Muffin", "stock": 12, "price": 8.00},
        7: {"name": "Smoked Salmon Sandwich", "stock": 15, "price": 17.00}
    },
    "Beverages": {
        1: {"name": "Espresso", "stock": 10, "price": 5.00},
        2: {"name": "Americano", "stock": 15, "price": 6.00},
        3: {"name": "Cafe Latte", "stock": 20, "price": 7.00},
        4: {"name": "Mocha", "stock": 15, "price": 8.00},
        5: {"name": "Caramel Latte", "stock": 15, "price": 8.00},
        6: {"name": "Macadamia Nut Latte", "stock": 12, "price": 8.00},
        7: {"name": "English Toffee Latte", "stock": 15, "price": 9.00}
    }
}

def display_menu():
    food_menu = []
    beverage_menu = []

    # Create formatted tables for foods and beverages
    for category, items in menu.items():
        for number, item in items.items():
            row = [number, item['name'], item['stock'], f"${item['price']}"]
            if category == "Foods":
                food_menu.append(row)
            elif category == "Beverages":
                beverage_menu.append(row)

    # Display formatted tables using tabulate
    print("Food Menu:")
    print(tabulate(food_menu, headers=["Number", "Name", "Stock", "Price"], tablefmt="rounded_grid"))

    print("\nBeverage Menu:")
    print(tabulate(beverage_menu, headers=["Number", "Name", "Stock", "Price"], tablefmt="rounded_grid"))

def add_menu_item(category, name, stock, price):
    name = name.title()  # Capitalize the first letter of each word in the name
    item_number = len(menu[category]) + 1
    menu[category][item_number] = {"name": name, "stock": stock, "price": price}
    print(f"New item '{name}' added to {category} menu.")

def remove_menu_item(category, item_number):
    if category in menu and item_number in menu[category]:
        del menu[category][item_number]
        # Create a copy of the menu items
        items = list(menu[category].items())
        # Clear the original menu
        menu[category].clear()
        # Re-populate the menu with re-numbered items
        for i, (key, item) in enumerate(items, start=1):
            menu[category][i] = item
            menu[category][i]["number"] = i
        print("Item removed successfully.")
    else:
        print("Item not found in the menu.")

def update_menu_item(category, item_number, stock=None, price=None):
    if category in menu and item_number in menu[category]:
        item = menu[category][item_number]
        if stock is not None:
            item['stock'] = stock
        if price is not None:
            item['price'] = price
        print("Item updated successfully.")
    else:
        print("Item not found in the menu.")

def get_category_choice():
    while True:
        category_choice = input("Enter the category (1) Foods or (2) Beverages): ")
        if category_choice == '1':
            return "Foods"
        elif category_choice == '2':
            return "Beverages"
        else:
            print("Invalid choice. Please enter 1 for Foods or 2 for Beverages.")

def admin_interface():
    # Define the correct password
    correct_password = "admin123"

    print("Welcome, Admin!")
    
    # Ask for the password
    password = input("Enter the password: ")

    # Check if the password is correct
    if password == correct_password:
        while True:
            display_menu()  # Display menu when entering admin interface
            print('''
    Please check availability item frequently
    1. Add Menu Item
    2. Remove Menu Item
    3. Update Menu Item
    4. Exit
            ''')
            choice = input("Enter your choice: ")

            if choice == '1':       #add_item
                while True:
                    category = get_category_choice()
                    try:
                        name = input("Enter the name of the item: ")
                        stock = int(input("Enter the stock: "))
                        price = float(input("Enter the price: "))
                        add_menu_item(category, name, stock, price)
                        confirm = input("Anything else? (Yes/No): ").lower()
                        while confirm not in ['yes', 'no']:
                            print("Invalid choice. Please enter 'Yes' or 'No'.")
                            confirm = input("Anything else? (Yes/No): ").lower()
                        if confirm != 'yes':
                            break  # Exit the loop if the user doesn't want to continue
                    except ValueError:
                        print("Invalid input. Please enter only number for stock and price.")

            elif choice == '2':           #removed_item
                while True:
                    category = get_category_choice()
                    try:
                        item_number = int(input("Enter the item number to remove: "))
                        remove_menu_item(category, item_number)
                        display_menu()
                        confirm = input("Anything else? (Yes/No): ").lower()
                        while confirm not in ['yes', 'no']:
                            print("Invalid choice. Please enter 'Yes' or 'No'.")
                            confirm = input("Anything else? (Yes/No): ").lower()
                        if confirm != 'yes':
                            break  # Exit the loop if the user doesn't want to continue
                    except ValueError:
                        print("Invalid input. Please enter valid item number!")

            elif choice == '3':   
                while True:
                    category = get_category_choice() 
                    try:
                        item_number = int(input("Enter the item number to update: "))
                        stock = int(input("Enter the new stock or the same: "))
                        price = float(input("Enter the new price or the same: "))
                        update_menu_item(category, item_number, stock=stock, price=price)
                        confirm = input("Anything else? (Yes/No): ").lower()
                        while confirm not in ['yes', 'no']:
                            print("Invalid choice. Please enter 'Yes' or 'No'.")
                            confirm = input("Anything else? (Yes/No): ").lower()
                        if confirm != 'yes':
                            break  # Exit the loop if the user doesn't want to continue
                    except ValueError:
                        print("Invalid input. Please enter only number for stock and price.")

            elif choice == '4':
                print("Exiting Admin Interface.")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 4.")
    else:
        print("Incorrect password. Access denied.")

def customer_interface(menu):
    cart = {}
    print("Welcome, Good People!")
    while True:
        display_menu()
        print('''
        Food is Memories, Happy Orders
1. Add to Cart
2. Remove From Cart
3. Modify Qty item
4. Lets Checkout!
5. Exit
        ''')
        choice = input("Enter your choice: ")
        if choice == '1':
            while True:
                category = get_category_choice() 
                try:
                    item_number = int(input("Enter the item number: "))
                    quantity = int(input("Enter the quantity: "))
                    add_to_cart(category, item_number, quantity, cart)
                    confirm = input("Anything else? (Yes/No): ").lower()
                    while confirm not in ['yes', 'no']:
                        print("Invalid choice. Please enter 'Yes' or 'No'.")
                        confirm = input("Anything else? (Yes/No): ").lower()
                    if confirm != 'yes':
                        break  # Exit the loop if the user doesn't want to continue
                except ValueError:
                    print("Invalid input. Please enter only number for item and quantity!")
        elif choice == '2':
            while True:
                if not cart:  # Check if the cart is empty
                    print("Your cart is empty.")
                    break
                print("This is your order: ")
                check_out(cart)
                try:
                    item_number = int(input("Enter the item number to remove from cart: "))
                    remove_from_cart(item_number, cart)
                except ValueError:
                    print("Invalid input. Please enter only number for item!")

        elif choice == '3':
            while True:
                if not cart:  # Check if the cart is empty
                    print("Your cart is empty.")
                    break
                print("This is your order: ")
                check_out(cart)
                try:
                    item_number = int(input("Enter the item number to modify: "))
                    quantity = int(input("Enter the new quantity: "))
                    modify_cart(item_number, quantity, cart)
                    confirm = input("Anything else? (Yes/No): ").lower()
                    while confirm not in ['yes', 'no']:
                        print("Invalid choice. Please enter 'Yes' or 'No'.")
                        confirm = input("Anything else? (Yes/No): ").lower()
                    if confirm != 'yes':
                        break  # Exit the loop if the user doesn't want to continue
                except ValueError:
                    print("Invalid input. Please enter only number for item and quantity!")
        elif choice == '4':
            if cart:  # Check if the cart is not empty
                print("This is your order: ")
                check_out(cart)
            else:
                print("Your cart is empty.")
        elif choice == '5':
            print("Exiting Customer Interface.")
            break
        else:
            print("Invalid choice.")

def check_out(cart):
    order_summary = []
    total_price = 0
    
    for idx, (item_number, item_info) in enumerate(cart.items(), start=1):
        name = item_info['name']
        quantity = item_info['quantity']
        price_per_item = item_info['price']
        item_total = quantity * price_per_item
        total_price += item_total
        
        order_summary.append([idx, name, quantity, f"${price_per_item:.2f}", f"${item_total:.2f}"])
    
    headers = ["No.", "Item Name", "Quantity", "Price Per Item", "Item Total"]
    
    print("\nOrder Summary:")
    print(tabulate(order_summary, headers=headers, tablefmt="rounded_grid"))
    print(f"\nTotal Price: ${total_price:.2f}")

    while True:
        try:
            money = float(input("Enter the amount of money: $"))
            if money < total_price:
                print("Insufficient amount. Please enter a higher amount.")
            else:
                change = money - total_price
                if change > 0:
                    print(f"Thank you for your purchase! Your change is ${change:.2f}.")
                else:
                    print("Thank you for your purchase! Exact amount received.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

def add_to_cart(category, item_number, quantity, cart):
    if item_number in menu[category]:
        item = menu[category][item_number]
        if item['stock'] >= quantity:
            if item_number in cart:
                cart[item_number]['quantity'] += quantity
            else:
                cart[item_number] = {'category': category, 'name': item['name'], 'price': item['price'], 'quantity': quantity}
            item['stock'] -= quantity
            print("Item added to cart.")
        else:
            print("Insufficient stock.")
    else:
        print("Item not found in the menu.")

def remove_from_cart(item_number, cart):
    if item_number in cart:
        item = cart.pop(item_number)
        menu[item['category']][item_number]['stock'] += item['quantity']
        print("Item removed from cart.")
    else:
        print("Item not found in the cart.")

def modify_cart(item_number, quantity, cart):
    if item_number in cart:
        item = cart[item_number]
        category = item['category']
        if quantity > 0:
            available_stock = menu[category][item_number]['stock']
            if quantity <= available_stock:
                # Adjust the cart quantity
                item['quantity'] = quantity
                # Update the stock in the menu
                menu[category][item_number]['stock'] = available_stock - quantity
                print("Cart updated.")
            else:
                print("Insufficient stock.")
        elif quantity == 0:
            remove_from_cart(item_number, cart)
        else:
            print("Invalid quantity. Please enter a positive number or 0 to remove from cart.")
    else:
        print("Item not found in the cart.")

def main():
    while True:
        print("\nWelcome to Cafe Dine-In Online Ordering System!")
        print("1. Admin Interface")
        print("2. Customer Interface")
        print("3. Exit")
        choice = input("Please select an interface: ")

        if choice == '1':
            admin_interface()
        elif choice == '2':
            customer_interface(menu)  # Pass the menu variable here
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

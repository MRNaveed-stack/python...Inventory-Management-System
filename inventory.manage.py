       #  This is a simple inventory management system
print("Welcome to the Simple Inventory Management System")

# List to store inventory items
inventory = []

# Function to add an item
def add_item(name, quantity, price):
    inventory.append({"name": name, "quantity": quantity, "price": price})
    return f"The item '{name}' has been added with a quantity of {quantity} at a price of ${price:.2f}"

# Function to view all items
def view_inventory():
    if not inventory:
        return "There is no item in the inventory."
    return "\n".join([f"{i + 1}. {item['name']} - Quantity: {item['quantity']}, Price: ${item['price']:.2f}" for i, item in enumerate(inventory)])

# Function to update an item
def update_item(item_number, quantity=None, price=None):
    if item_number < 1 or item_number > len(inventory):
        return "Invalid item number."
    if quantity is not None:
        inventory[item_number - 1]['quantity'] = quantity
    if price is not None:
        inventory[item_number - 1]['price'] = price
    return f"The item {item_number} has been updated successfully."

# Function to delete an item
def delete_item(item_number):
    if item_number < 1 or item_number > len(inventory):
        return "Invalid item number."
    removed_item = inventory.pop(item_number - 1)
    return f"The item '{removed_item['name']}' has been deleted."
def calculate_total_inventory_value():
    total_value = sum(item['quantity']*item['price'] for item in inventory)
    return f"total inventory value: $ {total_value} "

# Main loop
while True:
    print("\nMenu")
    print("1: Add item to inventory")
    print("2: View inventory")
    print("3: Update item in inventory")
    print("4: Delete item from inventory")
    print("5:calculate the total innventory value")
    print("6: Exit the system")
    
    choice = input("Enter a choice (1-6): ")
    
    if choice == "1":
        name = input("Enter the name of the item: ")
        try:
            quantity = int(input("Enter the quantity: "))
            price = float(input("Enter the price: "))
            print(add_item(name, quantity, price))
        except ValueError:
            print("Invalid input. Please enter a valid quantity and price.")
    
    elif choice == "2":
        print("Current Inventory:")
        print(view_inventory())
    
    elif choice == "3":
        try:
            item_number = int(input("Enter the item number to update: "))
            new_quantity = input("Enter new quantity (leave blank to keep current): ")
            new_price = input("Enter new price (leave blank to keep current): ")
            
            if new_quantity == "":
                new_quantity = None
            else:
                new_quantity = int(new_quantity)
            
            if new_price == "":
                new_price = None
            else:
                new_price = float(new_price)
            
            print(update_item(item_number, new_quantity, new_price))
        except ValueError:
            print("Invalid input. Please enter a valid item number.")
    
    elif choice == "4":
        try:
            item_number = int(input("Enter the item number to delete: "))
            print(delete_item(item_number))
        except ValueError:
            print("Invalid input. Please enter a valid item number.")
    
    elif choice == "5":
        print(calculate_total_inventory_value())

    elif choice == "6":
        print("exiting the system")
        break
    
    else:
        print("Invalid choice. Please select an option from 1 to 5.")
        #welcome to this inventory system
print("Welcome to the Simple Inventory Management System")

# List to store inventory items
inventory = []

# Function to add an item
def add_item(name, quantity, price):
    inventory.append({"name": name, "quantity": quantity, "price": price})
    return f"The item '{name}' has been added with a quantity of {quantity} at a price of ${price:.2f}"

# Function to view all items
def view_inventory():
    if not inventory:
        return "There is no item in the inventory."
    return "\n".join([f"{i + 1}. {item['name']} - Quantity: {item['quantity']}, Price: ${item['price']:.2f}" for i, item in enumerate(inventory)])

# Function to update an item
def update_item(item_number, quantity=None, price=None):
    if item_number < 1 or item_number > len(inventory):
        return "Invalid item number."
    if quantity is not None:
        inventory[item_number - 1]['quantity'] = quantity
    if price is not None:
        inventory[item_number - 1]['price'] = price
    return f"The item {item_number} has been updated successfully."

# Function to delete an item
def delete_item(item_number):
    if item_number < 1 or item_number > len(inventory):
        return "Invalid item number."
    removed_item = inventory.pop(item_number - 1)
    return f"The item '{removed_item['name']}' has been deleted."

# Function to calculate the total inventory value
def calculate_total_inventory_value():
    total_value = sum(item['quantity'] * item['price'] for item in inventory)
    return f"Total inventory value: ${total_value:.2f}"

# Main loop
while True:
    print("\nMenu")
    print("1: Add item to inventory")
    print("2: View inventory")
    print("3: Update item in inventory")
    print("4: Delete item from inventory")
    print("5: Calculate the total inventory value")
    print("6: Exit the system")
    
    choice = input("Enter a choice (1-6): ")
    
    if choice == "1":
        name = input("Enter the name of the item: ")
        try:
            quantity = int(input("Enter the quantity: "))
            price = float(input("Enter the price: "))
            print(add_item(name, quantity, price))
        except ValueError:
            print("Invalid input. Please enter a valid quantity and price.")
    
    elif choice == "2":
        print("Current Inventory:")
        print(view_inventory())
    
    elif choice == "3":
        try:
            item_number = int(input("Enter the item number to update: "))
            new_quantity = input("Enter new quantity (leave blank to keep current): ")
            new_price = input("Enter new price (leave blank to keep current): ")
            
            if new_quantity == "":
                new_quantity = None
            else:
                new_quantity = int(new_quantity)
            
            if new_price == "":
                new_price = None
            else:
                new_price = float(new_price)
            
            print(update_item(item_number, new_quantity, new_price))
        except ValueError:
            print("Invalid input. Please enter a valid item number.")
    
    elif choice == "4":
        try:
            item_number = int(input("Enter the item number to delete: "))
            print(delete_item(item_number))
        except ValueError:
            print("Invalid input. Please enter a valid item number.")
    
    elif choice == "5":
        print(calculate_total_inventory_value())

    elif choice == "6":
        print("Exiting the system. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please select an option from 1 to 6.")

'''
    Inventory Tracker for CDAC Bookstore
    Scenario
    The CDAC Bookstore needs a backend helper module to manage books and their quantities. The inventory is stored in a 
    Python dictionary where keys are book titles (strings) and values are quantities in stock (non-negative integers).

    Problem Description
    Write a function manage_bookstore_inventory(inventory, action, book_title, quantity=0) that handles inventory operations 
    safely.

    The action parameter can be one of three options: "add", "sell", or "lookup".
    Add Action ("add"):
    Add the specified quantity to the existing stock of book_title.
    If the book is not in the inventory dictionary, add it as a new key with quantity as the value.
    Sell Action ("sell"):
    Decrease the stock of book_title by the specified quantity.
    If the book is not found in the inventory, print a message: Error: Book '<book_title>' not found in inventory. and make 
    no changes. (Do not let the program crash with a KeyError).
    If the requested quantity to sell exceeds the stock available, print: Error: Insufficient stock for '<book_title>'. 
    Available: <current_stock>. and make no changes.
    If the stock reaches exactly 0 after a successful sale, remove the book key from the inventory entirely.
    Lookup Action ("lookup"):
    Look up the stock quantity of book_title and return it.
    Use safe dictionary retrieval; if the book does not exist, return 0 without throwing a KeyError.
    The function must return the updated/current inventory dictionary.

    Example Walkthrough
    # Initial Inventory
    inventory = {"Python Basics": 10, "Learning AI": 5}

    # 1. Add Stock
    inventory = manage_bookstore_inventory(inventory, "add", "Python Basics", 5)
    # Result: {"Python Basics": 15, "Learning AI": 5}

    # 2. Sell Stock Safely (Missing Book)
    inventory = manage_bookstore_inventory(inventory, "sell", "Data Science 101", 1)
    # Console output: Error: Book 'Data Science 101' not found in inventory.

    # 3. Sell Stock (Insufficient)
    inventory = manage_bookstore_inventory(inventory, "sell", "Learning AI", 10)
    # Console output: Error: Insufficient stock for 'Learning AI'. Available: 5.

    # 4. Sell Stock (Exactly Zero Stock)
    inventory = manage_bookstore_inventory(inventory, "sell", "Learning AI", 5)
    # Result: {"Python Basics": 15}
'''
import os
def manage_bookstore_inventory(
        inventory: dict, action: str, book_title: str, quantity: int = 0
        ) -> dict: 
    if action == 'add':
        inventory[book_title] = inventory.get(book_title, 0) + quantity
    elif action == 'sell':
        if book_title not in inventory:
            print(f"Book '{book_title}' not found in inventory.")
        elif quantity > inventory[book_title]:
            print(f"Insufficient stock for '{book_title}'. Available: {inventory[book_title]}.")
        else:
            inventory[book_title] -= quantity
            if inventory[book_title] == 0:
                del inventory[book_title]
    elif action == 'lookup':
        stock = inventory.get(book_title, 0)
        print(f"Stock for '{book_title}' : {stock}")

    return inventory

def main():
    inventory = {"Python Basics": 10, "Learning AI": 5}
    print(f"Initial Inventory: {inventory}\n")

    # 1. Add Stock
    inventory = manage_bookstore_inventory(inventory, "add", "Python Basics", 5)
    print(f"After adding 5 'Python Basics': {inventory}\n")

    # 2. Sell Stock (Missing Book)
    inventory = manage_bookstore_inventory(inventory, "sell", "Data Science 101", 1)

    # 3. Sell Stock (Insufficient)
    inventory = manage_bookstore_inventory(inventory, "sell", "Learning AI", 10)

    # 4. Sell Stock (Exactly Zero Stock)
    inventory = manage_bookstore_inventory(inventory, "sell", "Learning AI", 5)
    print(f"After selling 5 'Learning AI': {inventory}\n")

    # 5. Lookup Stock
    manage_bookstore_inventory(inventory, "lookup", "Python Basics")
    manage_bookstore_inventory(inventory, "lookup", "Nonexistent Book")


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("*" * 80)
    print(f"{' Inventory Tracker for CDAC Bookstore ':^80}")
    print("-" * 80)
    main()
    print("-" * 80)
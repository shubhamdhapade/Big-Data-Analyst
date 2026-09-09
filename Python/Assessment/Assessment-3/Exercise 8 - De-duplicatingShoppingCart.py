'''
    De-duplicating Shopping Cart
    Scenario: An online shopping cart has duplicate items due to double-clicks: 
    ["apple", "banana", "apple", "orange", "banana", "banana"]. Write a program that processes the list and removes 
    all duplicate items, but keeps the first occurrence of each item in its original order. Print the cleaned cart.

    Hardcoded Input: cart = ["apple", "banana", "apple", "orange", "banana", "banana"]
    Sample Output: ['apple', 'banana', 'orange']
'''

import os

def deduplicate_cart(cart: list[str]) -> list[str]:
    return list(dict.fromkeys(cart))

def main():
    cart = ["apple", "banana", "apple", "orange", "banana", "banana"]
    cleaned_cart = deduplicate_cart(cart)
    
    print(f"Original Cart: {cart}")
    print(f"Cleaned Cart:  {cleaned_cart}")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("*" * 80)
    print(f"{' De-duplicating Shopping Cart ':^80}")
    print("-" * 80)
    main()
    print("-" * 80)
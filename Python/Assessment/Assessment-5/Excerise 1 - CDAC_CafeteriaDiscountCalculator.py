'''
    CDAC Cafeteria Discount Calculator
    Scenario
    The CDAC Cafeteria needs a modular pricing function to calculate student bills. The cafeteria offers main combo meals, 
    optional side-dishes, standard tax rates, promotional discounts, and delivery charges.

    Problem Description
    Write a function named calculate_cafeteria_bill(base_price, *items, tax_rate=0.05, discount=0.0, delivery_fee=0.0) that 
    calculates the final bill.

    base_price (float): The cost of the main combo meal.
    *items (floats): A variable-length positional argument list representing prices of additional side items.
    tax_rate (float): The tax percentage (default 0.05 for 5% tax). This must be a keyword-only parameter.
    discount (float): A percentage value (e.g., 10.0 represents a 10% discount, default 0.0) applied directly to the subtotal 
    before taxes.
    delivery_fee (float): A flat shipping surcharge added to the final total after taxes (default 0.0).
    Calculation Rules:

    Sum the base_price and all side item prices (*items) to compute the raw subtotal.
    Deduct the discount from the raw subtotal to compute the discounted subtotal: 
    Discounted Subtotal =  Raw Subtotal * (1 - ( discount / 100))
    Compute the tax value by multiplying the discounted subtotal by tax_rate.
    Add the tax and delivery_fee to the discounted subtotal to get the final bill.
    Return the final total rounded to 2 decimal places.
    Example Walkthrough
    # 1. Standard meal, no sides, default tax, no discount, no delivery
    total1 = calculate_cafeteria_bill(100.0)
    # Subtotal = 100.0
    # Tax = 100.0 * 0.05 = 5.0
    # Return: 105.00

    # 2. Meal with sides, custom tax rate, 10% discount, flat delivery fee
    total2 = calculate_cafeteria_bill(100.0, 20.0, 30.0, tax_rate=0.08, discount=10.0, delivery_fee=15.0)
    # Raw Subtotal = 100.0 + (20.0 + 30.0) = 150.0
    # Discounted Subtotal = 150.0 * (1 - 10/100) = 135.0
    # Tax = 135.0 * 0.08 = 10.8
    # Final Total = 135.0 + 10.8 + 15.0 = 160.8
    # Return: 160.80
'''

import os
def calculate_cafeteria_bill(base_price, *items, tax_rate=0.05, discount=0.0, delivery_fee=0.0):
    raw_subtotal = base_price + sum(items)
    discounted_subtotal = raw_subtotal * (1 - (discount / 100))
    tax = discounted_subtotal * tax_rate
    final_total = discounted_subtotal + tax + delivery_fee
    return round(final_total, 2)
def main():
    total1 = calculate_cafeteria_bill(100.0)
    print(f"Total 1: {total1:.2f}")
    total2 = calculate_cafeteria_bill(100.0, 20.0, 30.0, tax_rate=0.08, discount=10.0, delivery_fee=15.0)
    print(f"Total 2: {total2:.2f}")
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("*" * 80)
    print(f"{' CDAC Cafeteria Discount Calculator ':^80}")
    print("-" * 80)
    main()
    print("-" * 80)
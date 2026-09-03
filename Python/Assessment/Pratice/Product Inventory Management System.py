# Product Inventory Management System

products = []


# --------------------------------------------------
# 1. ADD PRODUCT
# --------------------------------------------------
def add_product():
    print("\n===== ADD PRODUCT =====")

    # Name validation
    while True:
        name = input("Enter product name: ").strip()

        if name != "":
            break

        print("Error: Name cannot be empty.")

    # Category validation
    while True:
        category = input("Enter category: ").strip()

        if category != "":
            break

        print("Error: Category cannot be empty.")

    # Price validation
    while True:
        try:
            price = float(input("Enter price: "))

            if price > 0:
                break

            print("Error: Price must be greater than 0.")

        except ValueError:
            print("Error: Please enter a valid number.")

    # Quantity validation
    while True:
        try:
            quantity = int(input("Enter quantity: "))

            if quantity >= 0:
                break

            print("Error: Quantity must be >= 0.")

        except ValueError:
            print("Error: Please enter a valid integer.")

    # Generate ID
    if len(products) == 0:
        product_id = 1
    else:
        product_id = products[-1]["id"] + 1

    # Create dictionary
    product = {
        "id": product_id,
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity
    }

    # Add dictionary to list
    products.append(product)

    print("\nProduct added successfully!")
    print("Product ID:", product_id)


# --------------------------------------------------
# 2. VIEW ALL PRODUCTS
# --------------------------------------------------
def view_products():
    print("\n===== ALL PRODUCTS =====")

    if len(products) == 0:
        print("No products available.")
        return

    print("-" * 80)
    print(
        f"{'ID':<5}"
        f"{'Name':<20}"
        f"{'Category':<20}"
        f"{'Price':<15}"
        f"{'Quantity':<10}"
    )
    print("-" * 80)

    for product in products:
        print(
            f"{product['id']:<5}"
            f"{product['name']:<20}"
            f"{product['category']:<20}"
            f"{product['price']:<15.2f}"
            f"{product['quantity']:<10}"
        )

    print("-" * 80)


# --------------------------------------------------
# 3. SEARCH PRODUCT
# --------------------------------------------------
def search_product():
    print("\n===== SEARCH PRODUCT =====")

    search = input(
        "Enter Product ID or Product Name: "
    ).strip()

    found = False

    # Search by ID
    try:
        product_id = int(search)

        for product in products:
            if product["id"] == product_id:
                print("\nProduct Found:")
                print("ID       :", product["id"])
                print("Name     :", product["name"])
                print("Category :", product["category"])
                print("Price    :", product["price"])
                print("Quantity :", product["quantity"])

                found = True
                break

    except ValueError:

        # Search by name
        for product in products:
            if search.lower() in product["name"].lower():

                print("\nProduct Found:")
                print("ID       :", product["id"])
                print("Name     :", product["name"])
                print("Category :", product["category"])
                print("Price    :", product["price"])
                print("Quantity :", product["quantity"])

                found = True

    if not found:
        print("\nProduct not found.")


# --------------------------------------------------
# 4. UPDATE PRODUCT
# --------------------------------------------------
def update_product():
    print("\n===== UPDATE PRODUCT =====")

    try:
        product_id = int(
            input("Enter Product ID to update: ")
        )

    except ValueError:
        print("Error: Product ID must be an integer.")
        return

    # Find product
    product = None

    for p in products:
        if p["id"] == product_id:
            product = p
            break

    if product is None:
        print("Product not found.")
        return

    print("\nCurrent Details:")
    print("Name     :", product["name"])
    print("Category :", product["category"])
    print("Price    :", product["price"])
    print("Quantity :", product["quantity"])

    # Update name
    while True:
        name = input(
            "Enter new name: "
        ).strip()

        if name != "":
            product["name"] = name
            break

        print("Error: Name cannot be empty.")

    # Update category
    while True:
        category = input(
            "Enter new category: "
        ).strip()

        if category != "":
            product["category"] = category
            break

        print("Error: Category cannot be empty.")

    # Update price
    while True:
        try:
            price = float(
                input("Enter new price: ")
            )

            if price > 0:
                product["price"] = price
                break

            print("Error: Price must be greater than 0.")

        except ValueError:
            print("Error: Enter a valid price.")

    # Update quantity
    while True:
        try:
            quantity = int(
                input("Enter new quantity: ")
            )

            if quantity >= 0:
                product["quantity"] = quantity
                break

            print("Error: Quantity must be >= 0.")

        except ValueError:
            print("Error: Enter a valid integer.")

    print("\nProduct updated successfully!")


# --------------------------------------------------
# 5. DELETE PRODUCT
# --------------------------------------------------
def delete_product():
    print("\n===== DELETE PRODUCT =====")

    try:
        product_id = int(
            input("Enter Product ID to delete: ")
        )

    except ValueError:
        print("Error: Product ID must be an integer.")
        return

    for product in products:

        if product["id"] == product_id:

            products.remove(product)

            print("\nProduct deleted successfully!")

            return

    print("\nProduct not found.")


# --------------------------------------------------
# 6. MAIN MENU
# --------------------------------------------------
def main():

    while True:

        print("\n")
        print("=" * 40)
        print(" PRODUCT INVENTORY MANAGEMENT SYSTEM")
        print("=" * 40)

        print("1. Add Product")
        print("2. View All Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Exit")

        print("=" * 40)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_product()

        elif choice == "2":
            view_products()

        elif choice == "3":
            search_product()

        elif choice == "4":
            update_product()

        elif choice == "5":
            delete_product()

        elif choice == "6":
            print("\nThank you for using the system!")
            break

        else:
            print("\nInvalid choice. Please select 1-6.")


# --------------------------------------------------
# PROGRAM START
# --------------------------------------------------
if __name__ == "__main__":
    main()
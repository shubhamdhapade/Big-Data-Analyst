# Library Book Management System
# Python Systems Programming - Flat File Catalog Management

FILE_PATH = "books.txt"


# ---------------------------------------------------------
# 1. ADD BOOK
# ---------------------------------------------------------
def add_book_entry(catalog: list[dict], next_id: int) -> int:
    print("\n===== Add New Book =====")

    # Title
    while True:
        title = input("Enter book title: ").strip()
        if title:
            break
        print("Title cannot be empty.")

    # Author
    while True:
        author = input("Enter author name: ").strip()
        if author:
            break
        print("Author cannot be empty.")

    # Genre
    while True:
        genre = input("Enter genre: ").strip()
        if genre:
            break
        print("Genre cannot be empty.")

    # Price
    while True:
        try:
            price = float(input("Enter price: "))

            if price > 0:
                break

            print("Price must be greater than 0.")

        except ValueError:
            print("Invalid price. Please enter a number.")

    # Copies
    while True:
        try:
            copies = int(input("Enter number of copies: "))

            if copies >= 0:
                break

            print("Copies cannot be negative.")

        except ValueError:
            print("Invalid copies. Please enter an integer.")

    book = {
        "id": next_id,
        "title": title,
        "author": author,
        "genre": genre,
        "price": price,
        "copies": copies
    }

    catalog.append(book)

    print(f"\nBook added successfully with ID: {next_id}")

    return next_id + 1


# ---------------------------------------------------------
# 2. RENDER / DISPLAY CATALOG
# ---------------------------------------------------------
def render_catalog(catalog: list[dict]) -> None:

    if not catalog:
        print("\nCatalog is empty.")
        return

    # If only one book exists, show detailed card
    if len(catalog) == 1:
        book = catalog[0]

        print("\n========== BOOK DETAILS ==========")
        print(f"ID       : {book['id']}")
        print(f"Title    : {book['title']}")
        print(f"Author   : {book['author']}")
        print(f"Genre    : {book['genre']}")
        print(f"Price    : ₹{book['price']:.2f}")
        print(f"Copies   : {book['copies']}")
        print("==================================")

        return

    # Multiple books - table
    print("\n" + "=" * 105)

    print(
        f"{'ID':<5}"
        f"{'Title':<30}"
        f"{'Author':<25}"
        f"{'Genre':<15}"
        f"{'Price':>12}"
        f"{'Copies':>10}"
    )

    print("-" * 105)

    for book in catalog:
        print(
            f"{book['id']:<5}"
            f"{book['title'][:28]:<30}"
            f"{book['author'][:23]:<25}"
            f"{book['genre'][:13]:<15}"
            f"{book['price']:>12.2f}"
            f"{book['copies']:>10}"
        )

    print("=" * 105)


# ---------------------------------------------------------
# 3. SEARCH BOOKS
# ---------------------------------------------------------
def query_books(catalog: list[dict], search_term: str) -> list[dict]:

    search_term = search_term.strip()

    # Search by ID
    try:
        book_id = int(search_term)

        return [
            book for book in catalog
            if book["id"] == book_id
        ]

    except ValueError:
        pass

    # Search by title or author
    search_term = search_term.lower()

    return [
        book for book in catalog
        if search_term in book["title"].lower()
        or search_term in book["author"].lower()
    ]


# ---------------------------------------------------------
# 4. UPDATE BOOK
# ---------------------------------------------------------
def modify_book_details(catalog: list[dict], book_id: int) -> bool:

    for book in catalog:

        if book["id"] == book_id:

            print("\n===== Update Book =====")
            print(f"Book: {book['title']}")

            # Update price
            while True:
                try:
                    price = float(
                        input(
                            f"Enter new price "
                            f"[Current: {book['price']:.2f}]: "
                        )
                    )

                    if price > 0:
                        book["price"] = price
                        break

                    print("Price must be greater than 0.")

                except ValueError:
                    print("Invalid price.")

            # Update copies
            while True:
                try:
                    copies = int(
                        input(
                            f"Enter new copies "
                            f"[Current: {book['copies']}]: "
                        )
                    )

                    if copies >= 0:
                        book["copies"] = copies
                        break

                    print("Copies cannot be negative.")

                except ValueError:
                    print("Copies must be an integer.")

            print("\nBook details updated successfully.")

            return True

    print(f"\nBook with ID {book_id} not found.")

    return False


# ---------------------------------------------------------
# 5. DELETE BOOK
# ---------------------------------------------------------
def delete_book(catalog: list[dict], book_id: int) -> bool:

    for book in catalog:

        if book["id"] == book_id:

            print("\n===== Delete Book =====")
            print(f"ID     : {book['id']}")
            print(f"Title  : {book['title']}")
            print(f"Author : {book['author']}")

            confirmation = input(
                "Are you sure you want to delete this book? (y/n): "
            ).strip().lower()

            if confirmation == "y":
                catalog.remove(book)

                print("\nBook deleted successfully.")

                return True

            print("\nDelete operation cancelled.")

            return False

    print(f"\nBook with ID {book_id} not found.")

    return False


# ---------------------------------------------------------
# 6. SAVE CATALOG TO FILE
# ---------------------------------------------------------
def sync_catalog_to_file(
    filepath: str,
    catalog: list[dict]
) -> None:

    try:
        with open(filepath, "w") as file:

            for book in catalog:

                line = (
                    f"{book['id']}|"
                    f"{book['title']}|"
                    f"{book['author']}|"
                    f"{book['genre']}|"
                    f"{book['price']:.2f}|"
                    f"{book['copies']}\n"
                )

                file.write(line)

        print("\nCatalog saved successfully.")

    except OSError as error:
        print(f"\nError while saving file: {error}")


# ---------------------------------------------------------
# 7. LOAD CATALOG FROM FILE
# ---------------------------------------------------------
def load_catalog_from_file(filepath: str) -> list[dict]:

    catalog = []

    try:

        with open(filepath, "r") as file:

            for line in file:

                line = line.strip()

                if not line:
                    continue

                parts = line.split("|")

                if len(parts) != 6:
                    print("Skipping invalid record:", line)
                    continue

                try:

                    book = {
                        "id": int(parts[0]),
                        "title": parts[1],
                        "author": parts[2],
                        "genre": parts[3],
                        "price": float(parts[4]),
                        "copies": int(parts[5])
                    }

                    catalog.append(book)

                except ValueError:
                    print("Skipping invalid record:", line)

        print("\nCatalog loaded successfully.")

    except FileNotFoundError:
        print("\nbooks.txt not found.")
        print("Starting with an empty catalog.")

    except OSError as error:
        print(f"\nError while loading file: {error}")

    return catalog


# ---------------------------------------------------------
# 8. GET NEXT ID
# ---------------------------------------------------------
def get_next_id(catalog: list[dict]) -> int:

    if not catalog:
        return 1

    return max(book["id"] for book in catalog) + 1


# ---------------------------------------------------------
# 9. MAIN MENU
# ---------------------------------------------------------
def main():

    catalog = []
    next_id = 1

    while True:

        print("\n")
        print("=" * 50)
        print("       LIBRARY BOOK MANAGEMENT SYSTEM")
        print("=" * 50)

        print("1. Add Book")
        print("2. View Catalog")
        print("3. Search Books")
        print("4. Update Details")
        print("5. Delete Book")
        print("6. Save to File")
        print("7. Load from File")
        print("8. Exit")

        print("=" * 50)

        choice = input("Enter your choice: ").strip()

        # -------------------------------------------------
        # OPTION 1 - ADD
        # -------------------------------------------------
        if choice == "1":

            next_id = add_book_entry(
                catalog,
                next_id
            )

        # -------------------------------------------------
        # OPTION 2 - VIEW
        # -------------------------------------------------
        elif choice == "2":

            render_catalog(catalog)

        # -------------------------------------------------
        # OPTION 3 - SEARCH
        # -------------------------------------------------
        elif choice == "3":

            search_term = input(
                "\nEnter Book ID, Title or Author: "
            )

            results = query_books(
                catalog,
                search_term
            )

            if results:
                print("\nSearch Results:")
                render_catalog(results)
            else:
                print("\nNo matching books found.")

        # -------------------------------------------------
        # OPTION 4 - UPDATE
        # -------------------------------------------------
        elif choice == "4":

            try:
                book_id = int(
                    input("Enter Book ID to update: ")
                )

                modify_book_details(
                    catalog,
                    book_id
                )

            except ValueError:
                print("\nBook ID must be an integer.")

        # -------------------------------------------------
        # OPTION 5 - DELETE
        # -------------------------------------------------
        elif choice == "5":

            try:
                book_id = int(
                    input("Enter Book ID to delete: ")
                )

                delete_book(
                    catalog,
                    book_id
                )

            except ValueError:
                print("\nBook ID must be an integer.")

        # -------------------------------------------------
        # OPTION 6 - SAVE
        # -------------------------------------------------
        elif choice == "6":

            sync_catalog_to_file(
                FILE_PATH,
                catalog
            )

        # -------------------------------------------------
        # OPTION 7 - LOAD
        # -------------------------------------------------
        elif choice == "7":

            catalog = load_catalog_from_file(
                FILE_PATH
            )

            next_id = get_next_id(catalog)

        # -------------------------------------------------
        # OPTION 8 - EXIT
        # -------------------------------------------------
        elif choice == "8":

            print("\nThank you for using Library Book Management System.")
            break

        else:

            print("\nInvalid choice. Please select 1-8.")


# ---------------------------------------------------------
# PROGRAM START
# ---------------------------------------------------------
if __name__ == "__main__":
    main()
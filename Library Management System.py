# Library books list
books = ["The Alchemist", "1984", "To Kill a Mockingbird"]

# Borrowed books dictionary: {book_name: borrower}
borrowed = {}

# Main loop
while True:
    print("\n--- Library Management System ---")
    print("1. Display Available Books")
    print("2. Borrow a Book")
    print("3. Return a Book")
    print("4. Add a New Book")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == "1":
        print("\nAvailable Books:")
        for book in books:
            print("-", book)
        if not books:
            print("No books available right now.")
    
    elif choice == "2":
        print("\nWhich book do you want to borrow?")
        book_to_borrow = input("Enter book name: ")
        if book_to_borrow in books:
            name = input("Enter your name: ")
            books.remove(book_to_borrow)
            borrowed[book_to_borrow] = name
            print("You have borrowed:", book_to_borrow)
        else:
            print("Book not available or already borrowed.")
    
    elif choice == "3":
        print("\nWhich book are you returning?")
        book_to_return = input("Enter book name: ")
        if book_to_return in borrowed:
            books.append(book_to_return)
            del borrowed[book_to_return]
            print("Thank you for returning:", book_to_return)
        else:
            print("That book was not borrowed or doesn't belong to this library.")
    
    elif choice == "4":
        new_book = input("Enter the name of the book to add: ")
        books.append(new_book)
        print("Book added successfully:", new_book)
    
    elif choice == "5":
        print("Exiting Library Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please select between 1 to 5.")

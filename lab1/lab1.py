# Program Name: Lab1.py (use the name the program is saved as)
# Course: IT1113/Section W03
# Student Name: Ronnie Vincenty
# KSU Email Address: rvince13@students.kennesaw.edu
# Assignment Lab Number: 1
# Due Date: 01/19/2025
# # Purpose: What does the program do(in a few sentences)? This program takes user input to create an array of books:prices, then creates a receipt listing and adding the prices/names

#establishes the bookstore function
def bookstore_checkout():
    print("Welcome to our bookstore!")
    num_books = 6
    books = []
    total_price = 0.0

#iterates through the range of books, for this example 6 books, establishing the array for later use.
    for i in range(num_books):
        title = input(f"enter the book title {i+1}: ").strip()
        price = float(input(f"enter the price of '{title}': $"))
        books.append((title, price))

#prints a receipt for the user, multiplying the spaces/dashes for cleaner code.
    print("Purchase Receipt!")
    print(f"Book Title:"+" " * 5 + "Price:($)")
    print("-" * 30)

#concatonate all user inputs together and present the final price.
    for title, price in books:
        print(f"{title:20}  ${price:.2f}")
        total_price += price

    print("-" * 30)
    print(f"TOTAL: " + " " * 15 + f"${total_price:.2f}")

bookstore_checkout()

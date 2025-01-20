# Program Name: Lab_1.py (use the name the program is saved as)
# Course: IT1113/Section XXX
# Student Name: Ronnie Vincenty
# KSU Email Address: rvince13@students.kennesaw.edu
# Assignment Lab Number: 1
# Due Date: 01/19/2025
# # Purpose: What does the program do(in a few sentences)?


def bookstore_checkout():
    print("Welcome to our bookstore!")
    num_books = 6
    books = []
    total_price = 0.0

    for i in range(num_books):
        title = input(f"enter the book title {i+1}: ").strip()
        price = float(input(f"enter the price of '{title}': $"))
        books.append((title, price))

    print("Purchase Receipt!")
    print(f"Book Title:"+" " * 5 + "Price:($)")
    print("-" * 30)

    for title, price in books:
        print(f"{title:20}  ${price:.2f}")
        total_price += price

    print("-" * 30)
    print(f"TOTAL: " + " " * 15 + f"${total_price:.2f}")

bookstore_checkout()

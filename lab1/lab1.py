#creating the function
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
    print(f"Book Title:"+" " * 15 + "Price:($)")
    print("-" * 20)

    for title, price in books:
        print(f"{title:20}  ${price:.2f}")
        total_price += price

    print("-" * 20)
    print(f"TOTAL: " + " " * 15 + f"${total_price:.2f}")

bookstore_checkout()

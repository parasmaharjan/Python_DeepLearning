def main():
    # Create the empty list of the books that can be bought
    buy_book = []

    # Dictionary of all the book and its respective price
    book_list = {'Python': 50, 'Web': 30, 'C': 20, 'Java': 40, 'Embedded': 200, 'Calculus': 50, 'Statistics': 25}

    # Prompt user to enter minimum and maximum price range
    try:
        min_price = int(input("Enter min price: "))
        max_price = int(input("Enter max price: "))
    # Error non-integer value is input
    except ValueError:
        print("Only positive integer value allowed!")
        exit()

    # Ignoring negative input from user
    if (min_price < 0) | (max_price < 0) | (max_price < min_price):
        print("Invalid price range")
        exit()

    # Iterate through the items of dictionary
    for book, price in book_list.items():
        # Check if books in dictionary are in given range
        if price in range(min_price, max_price+1):
            # Append to list of book that can be bought
            buy_book.append(book)

    # Handling error if no book in list is found
    if not buy_book:
        print("No book found for price range ", min_price, "-", max_price)
    else:
        print("The list of book that you can buy for price range ", min_price, "-", max_price)
        for i in buy_book:
            print(i)


if __name__ == '__main__':
    print("Book search program\r\n")
    main()



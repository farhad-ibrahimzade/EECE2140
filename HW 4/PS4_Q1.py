from library import Library
from book import Book

lib = Library()

while True:

    print("--------------------------------------------------------------")

    print("Welcome to the Library program, please choose from one of the following options:")
    print("1 - Add a book to the library")
    print("2 - Remove a book from the library")
    print("3 - Display all books in the library")
    print("4 - Search for a specific book by ISBN")
    print("5 - Search for books by a specific author")
    print("6 - Search for books that cost less than a specific price")
    print()
    option = int(input("Please enter an option from above or enter 0 to exit: "))
    print()

    if (option == 0):
        break

    if option == 1:
        isbn = input("Please enter the ISBN: ")
        title = input("Please enter the book title: ")
        author = input("Please enter the book author: ")
        publisher = input("Please enter the book publisher: ")
        date = input("Please enter the book publishment date: ")
        price = int(input("Please enter the book price: "))
        lib.add_book(Book(isbn, title, author, publisher, date, price))
        print("The book has been added to the library")

    elif option == 2:
        isbn = input("Please enter the ISBN: ")
        lib.remove_book(isbn)
        print("The book has been removed from the library")

    elif option == 3:
        print("All the books in the library: ")
        print(lib)

    elif option == 4:
        isbn = int(input("Please enter the ISBN: "))
        print("Here is the result: ")
        book = lib.get_book_ISBN(isbn)
        if book == None:
            print("The book was not found")
        else:
            print(book)

    elif option == 5:
        author = input("Please enter the author's name: ")
        print("Here are the results: ")
        print(lib.get_book_author(author))

    elif option == 6:
        price = int(input("Please enter the book price: "))
        print("Here are the results: ")
        print(lib.get_book_price(price))

    print()
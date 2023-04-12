from book import Book

class Library:

    def __init__(self) -> None:
        """Initializes a new library
        """
        self.isbn_books = {}

    def add_book(self, book: Book):
        """Adds a new book to the library

        Args:
            book (Book): book to add
        """
        self.isbn_books[book.getISBN()] = book

    def remove_book(self, isbn: str):
        """Removes a book from the library by ISBN

        Args:
            isbn (str): ISBN of the book to remove
        """
        if isbn in self.isbn_books:
            self.isbn_books.pop(isbn)

    def get_book_ISBN(self, isbn: str) -> Book:
        """Returns a book from the library by ISBN

        Args:
            isbn (str): ISBN of the book to return

        Returns:
            Book: book
        """
        if isbn in self.isbn_books:
            return self.isbn_books[isbn]
        else:
            return None
        
    def get_book_author(self, author: str) -> str:
        """Returns book(s) from library by author

        Args:
            author (str): author of book(s)

        Returns:
            str: book(s) by author
        """
        return "".join(str(book) + "\n" for book in self.isbn_books.values() if book.getAuthors() == author)
        
    def get_book_price(self, price: float) -> str:
        """Returns book(s) below a specified price

        Args:
            price (float): book price

        Returns:
            str: book(s)  below specified price
        """
        return "".join(str(book) + "\n" for book in self.isbn_books.values() if book.getPrice() < price)

    def __str__(self) -> str:
        """Returns all books in the library in a string

        Returns:
            str: All books in the library
        """
        return "".join(str(book) + "\n" for book in self.isbn_books.values())
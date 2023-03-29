class Book:

    def __init__(self, isbn: str, title: str, authors: str, publisher: str, date: str, price: float) -> None:
        """Create a new book with ISBN, Title, Authors, Publisher, Publication Date and Price

        Args:
            isbn (str): ISBN of the book
            title (str): Title of the book
            authors (str): Authors of the book
            publisher (str): Publisher of the book
            date (str): Publication date of the book
            price (float): Price of the book
        """
        self.isbn = isbn
        self.title = title
        self.author = authors
        self.publisher = publisher
        self.date = date
        self.price = price

    # Getter methods

    def get_ISBN(self) -> str:
        """Returns the ISBN of a book

        Returns:
            str: book ISBN
        """
        return self.isbn

    def get_title(self) -> str:
        """Returns the title of a book

        Returns:
            str: book title
        """
        return self.title
    
    def get_authors(self) -> str:
        """Returns the authors of a book

        Returns:
            str: book authors
        """
        return self.author
    
    def get_Publisher(self) -> str:
        """Returns the publisher of the book

        Returns:
            str: book publisher
        """
        return self.publisher
    
    def get_date(self) -> str:
        """Returns the publication date of the book

        Returns:
            str: book publication date
        """
        return self.date
    
    def get_price(self) -> float:
        """Returns the price of the book

        Returns:
            float: book price
        """
        return self.price
    
    # Setter methods
    
    def set_ISBN(self, isbn: str):
        """Sets the book ISBN to a new value

        Args:
            isbn (str): New ISBN
        """
        self.isbn = isbn

    def set_title(self, title: str):
        """Sets the book title to a new value

        Args:
            title (str): New title
        """
        self.title = title
    
    def set_authors(self, authors: str):
        """Sets the book authors to a new value

        Args:
            authors (str): New authors
        """
        self.author = authors
    
    def set_publisher(self, publisher: str):
        """Sets the book publisher to a new value

        Args:
            publisher (str): New publisher
        """
        self.publisher = publisher
    
    def set_date(self, date: str):
        """Sets the book date to a new value

        Args:
            date (str): New date
        """
        self.date = date
    
    def set_price(self, price: float):
        """Sets the book price to a new value

        Args:
            price (float): New price
        """
        self.price = price
    

    def __str__(self) -> str:
        """Returns the information about the book in a string

        Returns:
            str: Information about the book
        """
        return f"{self.title} by {self.author}. Published by {self.publisher} on {self.date}. Price: {self.price}. ISBN: {self.isbn}"
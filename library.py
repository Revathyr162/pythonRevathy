class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.is_checked_out = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def find_books_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def checkout_book(self, title):
        book = self.find_book_by_title(title)
        if book and not book.is_checked_out:
            book.is_checked_out = True
            return book
        return None

    def return_book(self, title):
        book = self.find_book_by_title(title)
        if book and book.is_checked_out:
            book.is_checked_out = False
            return book
        return None

class User:
    def __init__(self, name):
        self.name = name

# Example usage:
library = Library()

book1 = Book("Python Programming", "John Doe", "Programming")
book2 = Book("Data Structures and Algorithms", "Jane Smith", "Computer Science")

library.add_book(book1)
library.add_book(book2)

user = User("Alice")

borrowed_book = library.checkout_book("Python Programming")
if borrowed_book:
    print(f"{user.name} has borrowed '{borrowed_book.title}' by {borrowed_book.author}.")
else:
    print("The book is not available.")

returned_book = library.return_book("Python Programming")
if returned_book:
    print(f"{user.name} has returned '{returned_book.title}' by {returned_book.author}.")
else:
    print("The book was not checked out or does not exist in the library.")

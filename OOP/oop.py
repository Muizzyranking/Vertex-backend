# Requirements:
#
# Library:
# The library should maintain a collection of books.
# Users can borrow and return books.
# Track the number of copies available for each book.
#
# Book:
# Each book should have attributes like title, author, ISBN,
# and a number of copies.
# A method to display book details.
#
# User:
# Each user should have attributes like name, user ID,
# and a list of borrowed books.
# Methods for borrowing and returning books.

class Book:
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies

    def __str__(self):
        message = f"{self.title} by {self.author}\
        (ISBN: {self.isbn}) - {self.copies} copies available"
        return message

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Copies available: {self.copies}")


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if isinstance(book, Book):
            if book.copies > 0:
                self.borrowed_books.append(book)
                book.copies -= 1
                print(f"{self.name} borrowed {book.title}")
            else:
                print(f"{book.title} is not available")
        else:
            print(f"{book} is not a valid instance of Book")

    def return_book(self, book):
        if isinstance(book, Book):
            if book in self.borrowed_books:
                self.borrowed_books.remove(book)
                book.copies += 1
                print(f"{self.name} returned {book.title}")
            else:
                print(f"{self.name} did not borrow {book.title}")
        else:
            print(f"{book} is not a valid instance of Book")

    def view_borrowed_books(self):
        if len(self.borrowed_books) > 0:
            print(f"{self.name} has borrowed the fololwing books:")

            for book in self.borrowed_books:
                print(book)

        else:
            print(f"{self.name} has not borrowed any books")


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        if isinstance(book, Book):
            if book.title in self.books:
                self.books[book.title].copies += book.copies

            else:
                self.books[book.title] = book
            print(f"Added {book.copies} copies to {book.title} to the library")
        else:
            print(f"{book} is not a valid instance of Book")

    def remove_book(self, title):
        if title in self.books:
            del self.books[title]
            print(f"Removed {title} from the library")

        else:
            print(f"{title} not found in library")

    def find_book(self, title):
        book = self.books.get(title)
        print(f"{title}: {book}")

    def display_books(self):
        if len(self.books) > 0:
            print("Library Collections")
            for book in self.books.values():
                print(book)

        else:
            print("The library is empty")


book1 = Book("1984", "George Orwell", "WRN123456", 5)
book3 = Book("1984", "George Orwell", "WRN123456", 20)
book2 = Book("Pride and Prejudice", "Jane Austen", "WRN121771", 7)
lib = Library()
lib.add_book(book1)
print("-------------------------------------------------\n")
lib.add_book(book3)
print("-------------------------------------------------\n")
lib.add_book(book2)
print("-------------------------------------------------\n")
lib.display_books()
print("-------------------------------------------------\n")
lib.find_book("Pride and Prejudice")
print("-------------------------------------------------\n")
lib.display_books()
# book1.display_details()
# print("-------------------------------------------------\n")
# user1 = User("John", "UID001")
# user1.borrow_book(book1)
# user1.borrow_book(book2)
# book1.display_details()
# # print("-------------------------------------------------\n")
# # user1.return_book(book1)
# # book1.display_details()
# print("-------------------------------------------------\n")
# user1.view_borrowed_books()

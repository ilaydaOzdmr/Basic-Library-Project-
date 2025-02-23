# A simple library automation for 'Turkcell Gelecegi Yazan Kadınlar'
class Book:
    def __init__(self, title, author, pages, isbn):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author}, {self.pages} pages, ISBN: {self.isbn}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if any(b.isbn == book.isbn for b in self.books):
            raise ValueError(f"A book with ISBN {book.isbn} already exists in the library.")
        self.books.append(book)
        print(f"Book '{book.title}' added successfully.")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book '{book.title}' removed successfully.")
                return
        raise ValueError(f"No book found with ISBN {isbn}.")

    def show_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            for book in self.books:
                print(book)

if __name__ == "__main__":
    library = Library()
    
    book1 = Book("1984", "George Orwell", 328, "9780451524935")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 281, "9780061120084")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180, "9780743273565")

    try:
        library.add_book(book1)
        library.add_book(book2)
        library.add_book(book3)
        library.add_book(book1)  # This will raise an exception
    except ValueError as e:
        print(f"Error: {e}")

    library.show_books()

    try:
        library.remove_book("9780061120084")
        library.remove_book("1234567890")  # This will raise an exception
    except ValueError as e:
        print(f"Error: {e}")
    
    library.show_books()

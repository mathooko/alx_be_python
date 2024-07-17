from library_management import Book, Library

def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()

if __name__ == "__main__":
    main()

class Book:
    def __init__(self, title,author, _is_checked_out):

        self.title=title
        self.author=author
        self._is_checked_out=_is_checked_out
    class Library :
        def __init__(self):

            self._books= [] 
        def add_book(self):
             if isinstance(book, Book):#Checks whether object book is an instance of the Book class
                self.books.append(book)
        def check_out_book(self,title):
            self.title=title
        def return_book(self,title):
            self.title=title            
        def list_available_books(self):
                for book in self.books:
                    print(f"{self.title}")
            
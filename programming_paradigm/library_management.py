# from library_management import Book, Library

# def main():
#     # Setup a small library
#     library = Library()
#     library.add_book(Book("Brave New World", "Aldous Huxley"))
#     library.add_book(Book("1984", "George Orwell"))

#     # Initial list of available books
#     print("Available books after setup:")
#     library.list_available_books()

#     # Simulate checking out a book
#     library.check_out_book("1984")
#     print("\nAvailable books after checking out '1984':")
#     library.list_available_books()

#     # Simulate returning a book
#     library.return_book("1984")
#     print("\nAvailable books after returning '1984':")
#     library.list_available_books()

# if __name__ == "__main__":
#      main()

class Book:
    def __init__(self, title,author):

        self.title=title
        self.author=author
        self._is_checked_out= False

    def check_out_book(self,):
            if not self._is_cheecked_out:
                 self._is_checked_out=True
            #self.title=title
            return False
    
    def return_book(self):
            if self._is_checked_out==True:
                 self._is_checked_out = False
                # self.title=title
            return True          
class Library :
        def __init__(self):
            
            self._books = [] 

        def add_book(self, book):
             if isinstance(book, Book):#Checks whether object book is an instance of the Book class
                self._books.append(book)
                return True
             return False
        def check_out_book(self):
            if not self._is_cheecked_out:
                 self._is_checked_out=True
            #self.title=title
            return False
        def return_book(self):
            if self._is_checked_out==True:
                 self._is_checked_out = False
                 #self.title=title
            return True          
        def list_available_books(self):
                for book in self._books:
                    print(f"{self._books}")
            
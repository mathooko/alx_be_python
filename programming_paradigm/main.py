#Bank Account

# import sys
# from bank_account import BankAccount


# def main():
#     account = BankAccount(100)  # Example starting balance
#     if len(sys.argv) < 2:
#         print("Usage: python main.py <command>:<amount>")
#         print("Commands: deposit, withdraw, display")
#         sys.exit(1)

#     command, *params = sys.argv[1].split(':')
#     amount = float(params[0]) if params else None

#     if command == "deposit" and amount is not None:
#         account.deposit(amount)
#         print(f"Deposited: ${amount}")
#     elif command == "withdraw" and amount is not None:
#         if account.withdraw(amount):
#             print(f"Withdrew: ${amount}")
#         else:
#             print("Insufficient funds.")
#     elif command == "display":
#         account.display_balance()
#     else:
#         print("Invalid command.")

# if __name__ == "__main__":
#     main()

#Main for safe divide

import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()

#Main for library Management

# if __name__ == "__main__":
#     main()

# class Book:
#     def __init__(self, title,author, _is_checked_out):

#         self.title=title
#         self.author=author
#         self._is_checked_out=_is_checked_out
#     class Library :
#         def __init__(self):

#             self._books= [] 
#         def add_book(self):
#              if isinstance(book, Book):#Checks whether object book is an instance of the Book class
#                 self.books.append(book)
#         def check_out_book(self,title):
#             self.title=title
#         def return_book(self,title):
#             self.title=title            
#         def list_available_books(self):
#                 for book in self.books:
#                     print(f"{self.title}")
            
import sys
# from bank_account import BankAccount
class BankAccount:
    def __init__(self, account_balance):

        self.account_balance=account_balance

    def deposit(self,amount):
        account_balance+=amount
        return self.account_balance
    def withdraw(self,amount):
        if account_balance>=amount:
            account_balance-=amount
        else :
            print("Insufficient funds")
def display_balance(self):

     print(f"Current Balance: ${self.account_balance:.2f}")





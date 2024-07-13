import sys
# from bank_account import BankAccount
class BankAccount:
    def __init__(self, account_balance):

        self.account_balance=account_balance

    def deposit(amount):
        account_balance+=amount
    def withdraw(amount):
        if account_balance>=amount:
            account_balance-=amount
        else :
            print("Insufficient funds")
def display_balance():

    return ("Current balance:",account_balance)


import sys
# from bank_account import BankAccount
class BankAccount:
    def __init__(self, account_balance=0):

            self.account_balance = account_balance

    def deposit(self,amount):
        self.account_balance+=amount
        return self.account_balance

    def withdraw(self,amount):
        if self.account_balance >= amount:
            self.account_balance - amount
            return True
        else :
           # print("Insufficient funds. ")

            return False
    def display_balance(self):

        print(f"Current Balance: ${self.account_balance:.2f}")

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
def display_balance(self):

    return ("Current balance:",account_balance)


def main():
    account = BankAccount(100)  # Example starting balance
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()


class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} into account {self.account_number}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self.balance

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, holder_name, initial_balance=0):
        if account_number not in self.accounts:
            self.accounts[account_number] = Account(account_number, holder_name, initial_balance)
            print(f"Account {account_number} created for {holder_name} with initial balance {initial_balance}.")
        else:
            print("Account number already exists.")

    def get_account(self, account_number):
        return self.accounts.get(account_number)

# Example usage:
bank = Bank()

bank.create_account("123456", "Alice", 1000)
bank.create_account("789012", "Bob")

alice_account = bank.get_account("123456")
if alice_account:
    alice_account.deposit(500)
    alice_account.withdraw(200)
    print(f"Current balance for Alice: {alice_account.get_balance()}")
else:
    print("Alice's account not found.")

bob_account = bank.get_account("789012")
if bob_account:
    bob_account.deposit(2000)
    print(f"Current balance for Bob: {bob_account.get_balance()}")
else:
    print("Bob's account not found.")

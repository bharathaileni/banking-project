
from dsa import LinkedList, Stack

class Account:

    def __init__(self, account_number, owner_name, initial_balance=0.0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = initial_balance
        self.transaction_history = LinkedList()
        self.undo_stack = Stack()
        self.add_transaction(f"Account created with balance: {self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.undo_stack.push(self.balance)
            self.balance += amount
            self.add_transaction(f"Deposited: {amount}")
            print(f"Success! New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.undo_stack.push(self.balance)
            self.balance -= amount
            self.add_transaction(f"Withdrew: {amount}")
            print(f"Success! New balance: {self.balance}")

    def add_transaction(self, transaction_description):
        self.transaction_history.prepend(transaction_description)
    
    def undo_last_transaction(self):
        previous_balance = self.undo_stack.pop()
        if previous_balance is not None:
            self.balance = previous_balance
            self.add_transaction("Undo successful. Balance reverted.")
            print(f"Undo successful! Balance is now: {self.balance}")
        else:
            print("Nothing to undo.")

    def display_details(self):
        print(f"\n--- Account Details for {self.account_number} ---")
        print(f"Owner: {self.owner_name}")
        print(f"Balance: ${self.balance:.2f}")
        print("--- Transaction History (Newest First) ---")
        for transaction in self.transaction_history.get_history():
            print(f"  - {transaction}")
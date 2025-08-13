
import pickle
import random
from account import Account
from dsa import Queue, BST

DATA_FILE = "bank_data.pkl"

class Bank:

    def __init__(self, filename=DATA_FILE):
        self.filename = filename
        self.accounts = self.load_data()
        self.transfer_queue = Queue()

    def create_account(self, owner_name, initial_balance):
        while True:
            account_number = str(random.randint(1000, 9999))
            if account_number not in self.accounts:
                break
        new_account = Account(account_number, owner_name, initial_balance)
        self.accounts[account_number] = new_account
        print(f"Account created successfully! Your new account number is: {account_number}")
        return new_account

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def schedule_transfer(self, from_acc_num, to_acc_num, amount):
        transfer_details = (from_acc_num, to_acc_num, amount)
        self.transfer_queue.enqueue(transfer_details)
        print("Transfer scheduled successfully! It will be processed by an admin.")

    def process_transfers(self):
        if self.transfer_queue.is_empty():
            print("No pending transfers to process.")
            return
        
        print("\n--- Processing Scheduled Transfers ---")
        while not self.transfer_queue.is_empty():
            from_acc, to_acc, amount = self.transfer_queue.dequeue()
            print(f"Processing: ${amount} from {from_acc} to {to_acc}...")
            from_account_obj = self.get_account(from_acc)
            to_account_obj = self.get_account(to_acc)
            
            if from_account_obj and to_account_obj:
                if from_account_obj.balance >= amount:
                    # We reuse the existing withdraw/deposit methods
                    from_account_obj.withdraw(amount)
                    to_account_obj.deposit(amount)
                    print("...Success!")
                else:
                    print("...Failed: Insufficient funds.")
            else:
                print("...Failed: Invalid account number.")
        print("--- All transfers processed. ---")

    def display_accounts_sorted_by_balance(self):
        if not self.accounts:
            print("No accounts in the bank.")
            return

        bst = BST()
        for acc_num, account_obj in self.accounts.items():
            bst.insert(account_obj.balance, acc_num)
        
        print("\n--- Accounts Sorted by Balance (Lowest to Highest) ---")
        sorted_account_numbers = bst.in_order_traversal()
        for acc_num in sorted_account_numbers:
            acc = self.get_account(acc_num)
            print(f"  Account: {acc.account_number}, Owner: {acc.owner_name}, Balance: ${acc.balance:.2f}")

    def save_data(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self.accounts, file)
        print("\nData saved. Have a great day!")

    def load_data(self):
        try:
            with open(self.filename, "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            return {}
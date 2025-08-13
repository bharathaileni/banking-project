
from bank import Bank

def get_positive_float_input(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount <= 0:
                print("Amount must be positive. Please try again.")
                continue
            return amount
        except ValueError:
            print("Invalid input. Please enter a number.")

def account_menu(bank, account):
    while True:
        print(f"\n--- Welcome, {account.owner_name} (Account: {account.account_number}) ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Details & History")
        print("4. Schedule a Fund Transfer")
        print("5. Undo Last Transaction")
        print("6. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = get_positive_float_input("Enter amount to deposit: ")
            account.deposit(amount)
        elif choice == '2':
            amount = get_positive_float_input("Enter amount to withdraw: ")
            account.withdraw(amount)
        elif choice == '3':
            account.display_details()
        elif choice == '4':
            to_acc = input("Enter account number to transfer to: ")
            amount = get_positive_float_input("Enter amount to transfer: ")
            bank.schedule_transfer(account.account_number, to_acc, amount)
        elif choice == '5':
            account.undo_last_transaction()
        elif choice == '6':
            print("Logging out...")
            break
        else:
            print("Invalid choice.")

def main_menu(bank):
    while True:
        print("\n===== Welcome to the Console Bank! =====")
        print("1. Create New Account")
        print("2. Login to Existing Account")
        print("--- Admin Options ---")
        print("3. Process Scheduled Transfers")
        print("4. Display Accounts Sorted by Balance")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter your full name: ")
            balance = get_positive_float_input("Enter initial deposit amount: ")
            bank.create_account(name, balance)
        elif choice == '2':
            acc_num = input("Enter your account number: ")
            account = bank.get_account(acc_num)
            if account:
                account_menu(bank, account)
            else:
                print("Invalid account number.")
        elif choice == '3':
            bank.process_transfers()
        elif choice == '4':
            bank.display_accounts_sorted_by_balance()
        elif choice == '5':
            bank.save_data()
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    my_bank = Bank()
    main_menu(my_bank)
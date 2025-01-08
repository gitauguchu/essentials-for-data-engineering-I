from bank import  BankAccount

def create_account():
    account_number = input("Enter account number: ")
    account_holder = input("Enter account holder's name: ")
    initial_balance = float(input("Enter initial balance: "))
    return BankAccount(account_number, account_holder, initial_balance)

def perform_deposit(account):
    amount = float(input("Enter amount to deposit: "))
    account.deposit(amount)

def perform_withdrawal(account):
    amount = float(input("Enter amount to withdraw: "))
    account.withdraw(amount)

def check_balance(account):
    account.check_balance()

def view_transactions(account):
    account.view_transactions()

def main():
    print("Welcome to the basic banking system")
    account = create_account()
    print("Account created successfully!\n")

    while True:
        print("\nMenu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Transactions")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            perform_deposit(account)
        elif choice == '2':
            perform_withdrawal(account)
        elif choice == '3':
            check_balance(account)
        elif choice == '4':
            view_transactions(account)
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()
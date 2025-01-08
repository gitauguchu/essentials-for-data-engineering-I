class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transactions = []

    def __str__(self):
        return f"Account [{self.account_number}] - Holder: {self.account_holder} - Balance: ${self.balance}"
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited: ${amount}")
            print(f"${amount} deposited successfully")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                self.transactions.append(f"Withdrew: ${amount}")
                print(f"${amount} withdrawn successfully")
            else:
                print("Insufficient funds")
        else:
            print("Withdrawal amount must be positive")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")
        return self.balance
    
    def view_transactions(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)
            

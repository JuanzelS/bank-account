import random

class BankAccount:
    def __init__(self, full_name):
        self.full_name = full_name
        self.account_number = random.randint(10000000, 99999999)
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited: ${amount:.2f}, new balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Charging a $10 overdraft fee.")
            self.balance -= 10
        else:
            self.balance -= amount
        print(f"Amount withdrawn: ${amount:.2f}, new balance: ${self.balance:.2f}")

    def get_balance(self):
        print(f"Current balance: ${self.balance:.2f}")
        return self.balance

    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest
        print(f"Interest added: ${interest:.2f}, new balance: ${self.balance:.2f}")

    def print_statement(self):
        masked_account_number = "****" + str(self.account_number)[-4:]
        print(f"""
        {self.full_name}
        Account No.: {masked_account_number}
        Balance: ${self.balance:.2f}
        """)


# Example usage of the BankAccount class
if __name__ == "__main__":
    # Create a new account for Mitchell
    mitchell_account = BankAccount("Mitchell")

    # Deposit $400,000
    mitchell_account.deposit(400000)

    # Print account statement
    mitchell_account.print_statement()

    # Add interest to the account
    mitchell_account.add_interest()

    # Print account statement after adding interest
    mitchell_account.print_statement()

    # Withdraw $150
    mitchell_account.withdraw(150)

    # Print account statement after withdrawal
    mitchell_account.print_statement()

    # Create additional accounts as examples
    jane_account = BankAccount("Jane Doe")
    jane_account.deposit(2500)
    jane_account.print_statement()

    john_account = BankAccount("John Smith")
    john_account.deposit(500)
    john_account.add_interest()
    john_account.print_statement()

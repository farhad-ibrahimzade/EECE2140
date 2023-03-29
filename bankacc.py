class BankAccount:

    def __init__(self, customer_id: str, account_number: str, balance: float = 0):
        self.customer_id = customer_id
        self.account_number = account_number
        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        if amount <= self.balance:
            self.balance -= amount

        else:
            raise ValueError("Not enough balance in the account")

        
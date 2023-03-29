from bankacc import BankAccount

class SavingsAccount:

    def __init__(self, customer_id: str, account_number: str, balance: float, interest_rate: float) -> None:
        super.__init__(customer_id, account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self, amount: float):
        self.balance *=(1 + self.interest_rate)
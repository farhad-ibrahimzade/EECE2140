from bankacc import BankAccount

class CurrentAccount:

    def __init__(self, customer_id: str, account_number: str, balance: str, transaction_limit: float = 1000):
        super.__init__(customer_id, account_number, balance)
        self.transaction_limit = transaction_limit

    def withdraw(self, amount: float):
        if amount < self.transaction_limit:
            super.withdraw(amount)
        else:
            raise ValueError("Transaction over limit")
        
    

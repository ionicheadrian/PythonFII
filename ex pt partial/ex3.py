class BankAccount:
    def __init__ (self, balance=0):
        self.amount = balance
    def __str__(self):
        return f"Balance:${self.amount}"
    def deposit(self, amount: float):
        if amount > 0:
            self.amount=amount
    def withdraw(self, amount: float):
        if self.amount >= amount:
            self.amount-= amount
            print(f"S-au scos {amount} din contul dvs. Total {self.amount}")
        else:
            raise ValueError("NU AI VOIE !")
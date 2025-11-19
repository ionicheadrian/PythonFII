class BankAccount:
    def __init__(self, balance=0):
        self.balance=0
    def __str__(self):
        return f"Balance ${self.balance}"
    def deposit(self, x):
        if x >= 0:
            self.balance+=x
            print(f"Balance: {self.balance}")

    def withdraw(self, x):
        if self.balance - x > 0:
            self.balance=self.balance - x
            print(f"Balance: {self.balance}")


p=BankAccount(10)
p.deposit(10)
p.withdraw(5)
print(p)



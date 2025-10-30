class BankAccount:
    def __init__(self, holder : str, balance : float =0.0):
        self.holder = holder
        self.balance = float(balance)

    def deposit(self, amount : float):
            
        if amount < 0:
            print("eroare: suma este mai mica decat 0")
            return
        if amount == 0:
            print("eroare: suma nu poate sa fie 0")
            return
        self.balance += float(amount)

    def withdraw (self, amount: float):
        if amount < 0:
            print("eroare: suma este mai mica decat 0")
            return
        if amount == 0:
            print("eroare: suma nu poate sa fie 0")
        self.balance -= float(amount)
        
    def display_balance(self) :
        print(f"Soldul este : {self.balance}")


a = BankAccount("Adrian", 0)

a.deposit(10)
a.withdraw(2)
a.display_balance()
print("-"*10)
a.deposit(-1)
a.deposit(0)
a.display_balance()
print("-"*10)
a.withdraw(500)
a.withdraw(0)
a.withdraw(-1)
            

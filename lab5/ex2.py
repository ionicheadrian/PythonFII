class Product:
    def __init__(self, name : str, price: float, quantity : int):
        if name == "":
            print(f"Produsul are nevoie MACAR de un nume :D")
            return
        self.name = name
        if price >= 0:
            self.price = float(price)
        else:
            print(f"warning: produsul cu numele:{self.name} nu are pret valid!")
        if quantity >= 1:
            self.quantity = int(quantity)
        else:
            print(f"warning: produsul cu numele:{self.name} nu are quantity valida (quantity <= 0)!")
    
    def total_value(self):
        if self.quantity == 0:
            print("eroare: nu avem acest produs :(")
            return
        return self.price * self.quantity
    def update_quantity(self,new_quantity):
        if new_quantity <=0:
            print("eroare: nu ai cum sa adaugi ceva mai mic decat 0 :D")
            return
        self.quantity = new_quantity

    def description(self):
        print(f"Product:{self.name}, Price: {self.price}, Quantity: {self.quantity} lei, Total Value: {self.total_value()} lei")
        

a = Product("Pix", 5 ,10)

a.total_value()
a.update_quantity(2)
a.description()
a.update_quantity(10)
a.description()
print("-"*10)
b = Product("Test fara pret", -74, 10)
c = Product("Test  fara quantity", 10, -3)

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

class Invoice:
    def __init__(self):
        self.products = []
    
    def add_product(self,name: str, price: float ,quantity: int):
        self.products.append(Product(name,price,quantity))
    
    def total_value(self):
        s = 0 
        for p in self.products:
            s+= p.total_value()
        return s
    
    def most_expensive(self):
        if not self.products:
            print("eroare: navem produse :(")
            return
        return max(self.products, key=lambda p: p.price)
    
    def display(self):
        for p in self.products:
            p.description()
            print("-"*10)
        print(f"Pretul total este: {self.total_value()} lei")

def test_invoice_basic():
    print("== test_invoice_basic ==")
    inv = Invoice()
    inv.add_product("Mere", 3.5, 10)   # 35
    inv.add_product("Pix", 5.0, 2)     # 10
    print("invoice total (expected 45):", inv.total_value())
    me = inv.most_expensive()
    if me:
        print("cel mai scump (expected Pix):", me.name, me.price)
    print("displaying invoice:")
    inv.display()
    print()

def test_update_quantity_reflects_total():
    print("== test_update_quantity_reflects_total ==")
    inv = Invoice()
    inv.add_product("Mere", 3.0, 2)  # 6
    inv.add_product("Pix", 2.0, 3)   # 6 -> total 12
    print("initial total (expected 12):", inv.total_value())
    inv.products[0].update_quantity(10)  # Mere -> 30, new total 36
    print("after update (expected 36):", inv.total_value())
    print()


test_invoice_basic()
test_update_quantity_reflects_total()
















class Product:
    def __init__(self, name, price):
        print("Product Object is Created....!")
        self.name = name
        self.price = price
        print("-------------------")
P1=Product("Phone", 10000)
print(f"Name;{P1.name}")
print(f"Price:{P1.price}")




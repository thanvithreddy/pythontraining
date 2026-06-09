class Mobile:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color
    def display_details(self):
        print("Brand :", self.brand)
        print("Price :", self.price)
        print("Color :", self.color)
        print("-" * 25)
m1 = Mobile("Samsung", 25000, "Black")
m2 = Mobile("Apple", 80000, "White")
m3 = Mobile("OnePlus", 35000, "Blue")
m4 = Mobile("Vivo", 22000, "Red")
m5 = Mobile("Realme", 18000, "Green")
m1.display_details()
m2.display_details()
m3.display_details()
m4.display_details()
m5.display_details()

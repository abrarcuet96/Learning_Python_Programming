# Exercise_01:
# Make a Laptop class
# including the brand, name and price.

class Laptop:
    def __init__(self, brand, name, price):
        self.brand = brand
        self.name = name
        self.price = price
l1=Laptop('Asus', 'Vivobook', 12000)
print(l1.brand)
print(l1.name)
print(l1.price)
# Exercise_02:
# Apply discount(create an instance) on the laptop price.

class Laptop:
    def __init__(self, brand, name, price):
        self.brand = brand
        self.name = name
        self.price = price

    def apply_discount(self, discount):
        return f"Your discount price on {self.brand} {self.name} is {self.price - self.price*discount/100}"
        
l1=Laptop('Asus', 'Vivobook', 12000)
print(l1.apply_discount(60))
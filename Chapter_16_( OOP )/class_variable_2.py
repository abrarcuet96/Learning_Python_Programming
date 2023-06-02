class Laptop:
    discount=10
    def __init__(self, brand, name, price):
        self.brand = brand
        self.name = name
        self.price = price

    def apply_discount(self):
        # If we want to use the class variable individually,
        # we have to write self.discount instead of Laptop.discount.
        return f"Your discount price on {self.brand} {self.name} is {self.price - self.price*(self.discount)/100}"

l1=Laptop('Asus', 'Vivobook', 12000)
l2=Laptop('Asus', 'Ultrabook', 20000)
print(l1.apply_discount()) # for, Laptop 1 discount price 10% is available.
l2.discount=50 # We declare another discount offer for Laptop 2.
print(l2.apply_discount())
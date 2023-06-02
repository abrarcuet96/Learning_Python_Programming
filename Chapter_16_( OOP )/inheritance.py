class Phone: # base class/ parent class
    def __init__(self, brand, model, price):
        self.brand=brand
        self.model=model
        self.price=max(price,0)
    def make_a_call(self, phone_num):
        return f"calling {phone_num} ..."
    def full_name(self):
        return f"{self.brand} {self.model}"

# Inheritance:
class Smartphone(Phone): # child class
    def __init__(self, brand, model, price, ram, internal_memory, rear_camera):
        # two methods:
        # method_1: uncommon way
        # Phone.__init__(self,brand, model, price)
        # method_2:
        super().__init__(brand, model, price)
        self.ram=ram
        self.internal_memory=internal_memory
        self.rear_camera=rear_camera
    def make_a_call(self, phone_num):
        return f"calling {phone_num} ..."
    def full_name(self):
        return f"{self.brand} {self.model}"
    
phone=Phone('nokia', '1100', 1000)
smartphone=Smartphone('oneplus', '10', 3000, '6 gb', '64 gb', '24 mp')
print(phone.full_name())
print(smartphone.full_name())
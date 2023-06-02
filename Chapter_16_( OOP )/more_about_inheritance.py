# can we derive more than one class from base class?
# multilevel inheritance
# method resolution order
# method overriding
# isinstance(), issubclass()

class Phone: # base class/ parent class
    def __init__(self, brand, model, price):
        self.brand=brand
        self.model=model
        self.price=max(price,0)
    def make_a_call(self, phone_num):
        return f"calling {phone_num} ..."
    def full_name(self):
        return f"{self.brand} {self.model}"

class Smartphone(Phone): # child class
    def __init__(self, brand, model, price, ram, internal_memory, rear_camera):
        super().__init__(brand, model, price)
        self.ram=ram
        self.internal_memory=internal_memory
        self.rear_camera=rear_camera
    def make_a_call(self, phone_num):
        return f"calling {phone_num} ..."
    # method overriding:
    def full_name(self):
        return f"{self.brand} {self.model} and price is {self.price}"
# multilevel inheritance:    
class FlagshipPhone(Smartphone):
    def __init__(self, brand, model, price, ram, internal_memory, rear_camera, front_camera):
        super().__init__(brand, model, price, ram, internal_memory, rear_camera)
        self.front_camera=front_camera
    

phone=Phone('nokia', '1100', 1000)
smartphone=Smartphone('oneplus', '10', 3000, '6 gb', '64 gb', '24 mp')
flagshipphone=FlagshipPhone('oneplus', '16', 3000, '6 gb', '64 gb', '24 mp', '16 mp')
print(phone.full_name())
print(smartphone.full_name())
print(flagshipphone.full_name())

# method resolution order: It will show the order of how pyhton is searching the instructions in the class.
# print(flagshipphone.full_name())
# print(help(flagshipphone))

# isinstance(): To check wheather the object belongs to a particuler class or not.
print(isinstance(smartphone, Smartphone)) # True
print(isinstance(smartphone, FlagshipPhone)) # False

# issubclas(): To check wheather a subclass belongs to a particuler class or not.
print(issubclass(Smartphone,Phone)) # True
print(issubclass(Phone,Smartphone)) # False
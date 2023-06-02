# Encapsulation:
class Phone:
    def __init__(self, brand, model, price):
        self.brand=brand
        self.model=model
        self.price=price
    def make_a_call(self, phone_num):
        print(f"calling {phone_num} ...")
    def full_name(self):
        return f"{self.brand} {self.model}"
    def send_message(self):
        pass # twilio
## here, make_a_call, full_name, send_message are encapsulated in class Phone.
phone1=Phone('nokia', '1100', 2000)

# Abstraction:
l=[3,4,2,1]
l.sort() # here, sort is a complex function.
print(l)
# Hiding complexicity from user is called Abstraction.

## naming convention:
# _name --> convention of private name.
# __name__ --> dunder/magic method


# __name()--> is not a convention(Name Mangling)
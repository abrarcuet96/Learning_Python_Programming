class Phone:
    def __init__(self, brand, model, price):
        self.brand=brand
        self.model=model
        # if price>0:
        #     self.price=price
        # else:
        #     self.price=0
        self._price=max(price,0) # Now, Price cannot be less then 0
        # self.complete_specification= f"{self.brand} {self.model} and price is {self.price}"
    @property
    def complete_specification(self):
        return f"{self.brand} {self.model} and price is {self.price}"
    
    # using setter decorator to not to use negative in price.
    # before setter decorator we must write property decorator -->getter decorator.
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self,new_price):
        self._price=max(new_price,0)

    def make_a_call(self, phone_num):
        print(f"calling {phone_num} ...")
    def full_name(self):
        return f"{self.brand} {self.model}"
    

phone1=Phone('nokia', '1100', -2000) # here, price will show 0
print(phone1.brand)
print(phone1.model)
phone1.price=-500
print(phone1.price)
print(phone1.complete_specification)
# As we have used Property decorator we need not to write phone1.complete_specification()
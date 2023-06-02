# object/instance method:

class Person:
    def __init__(self, first_name, last_name, age):
        # here,
        # self--> object(p1)
        # attributes--> first_name, last_name, age
        # instance variables:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    # define method:
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
p1=Person('Abrar', 'Haider', 23)
Full_Name=p1.full_name()
print(Full_Name)
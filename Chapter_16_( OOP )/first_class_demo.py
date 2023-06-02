class Person:
    def __init__(self, first_name, last_name, age):
        # here,
        # self--> object(p1)
        # attributes--> first_name, last_name, age
        # instance variables:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
p1=Person('Abrar', 'Haider', 23)

print(p1.first_name)
print(p1.last_name)
print(p1.age)
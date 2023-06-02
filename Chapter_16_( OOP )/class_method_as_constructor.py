class Person:
    def __init__(self, first_name, last_name, age):
        # here,
        # self--> object(p1)
        # attributes--> first_name, last_name, age
        # instance variables:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    # two separate a string;
    @classmethod
    def from_string(cls,string):
        first,last,age=string.split(',')
        return cls(first,last,age)
    # define method:
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    
p1=Person.from_string('Abrar,Haider,23')
print(p1.full_name())
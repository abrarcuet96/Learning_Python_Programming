# Exercise_03:
# count how many time instance is called.
class Person:
    count_instance=0
    def __init__(self, first_name, last_name, age):
        # here,
        # self--> object(p1)
        # attributes--> first_name, last_name, age
        Person.count_instance +=1
        # instance variables:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

p1= Person('Abrar', "Haider", 23)
p2= Person('Abrar', "Haider", 23)
p3= Person('Abrar', "Haider", 23)
print(Person.count_instance)
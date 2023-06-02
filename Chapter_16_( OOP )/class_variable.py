# Circle--> area, circumference

class Circle:
    pi=3.1416 # It is a class variable/ class instance.
    def __init__(self, radius):
        self.radius=radius

    def area(self):
        return f"Area is {(Circle.pi)*(self.radius**2)}"
    def circum(self):
        return f"Circumference is {2*(Circle.pi)*(self.radius)}"
    
c= Circle(4)
print(c.area())
print(c.circum())
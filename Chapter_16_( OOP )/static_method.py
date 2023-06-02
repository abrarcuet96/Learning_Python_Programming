class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    # static method doesnot have any link with other portions of class.
    @staticmethod
    def hello():
        print("Hello, statics method called")
    # define method:
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

Person.hello()
class Animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        raise NotImplementedError('you have to define this mehtod in subclasses')
        # it will force to check the function in subclasses

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
    def sound(self):
        return 'bhou bhou'
class Cat(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
    def sound(self):
        return 'meow meow'

doggy= Dog('boony','pug')
print(doggy.sound())
meeow= Cat('boony','pug')
print(meeow.sound())
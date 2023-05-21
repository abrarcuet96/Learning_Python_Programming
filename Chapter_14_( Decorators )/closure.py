# Closure--> first class funcion.
def to_power(x):
    def calc_power(n):
        return n**x
    return calc_power
square=to_power(2)
print(square(3))
cube=to_power(3)
print(cube(3))

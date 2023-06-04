# def add(a,b):
#     return a+b
# print(add(5,4))

# if we give string instead of integer-->
def add(a,b):
    if (type(a) is int) and (type(b) is int):
        return a+b
    raise TypeError('oops you are passing wrong data type to function')
print(add('4','3'))
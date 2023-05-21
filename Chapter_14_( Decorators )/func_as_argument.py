# map function:
l=[1,2,3,4,5]
def square(a):
    return a**2
print(list(map(square,l))) ## here, function is used as an argument.
# Or, use lambda:
print(list(map(lambda a: a**2,l))) 

### Creating a map function:
def my_map(func,l):
    new_list=[]
    for item in l:
        new_list.append(func(item))
    return new_list
print(my_map(square,l))
# Or, use Lambda function:
print(my_map(lambda a: a**3,l))
# Or, use list comprehension:
def my_map2(func,l):
    return [func(item) for item in l]
print(my_map2(lambda a: a**4,l))

# syntax error:
# def func: [correction--> func():]
#     pass

# indentation error:
# def func():
#     print('hello')
#   print('world')

# name error:
# print(name) # no name is defined here.

# type error: 
# if we perform any operation with wrong type.
# print(5+ 'abrar')

# index error:
# l=[1,2,3]
# print([4]) # here, index is out of range.

# value error:
# s='abc'
# print(int(s)) --> abc can't be convert to string

# attribute error:
# l=[1,2,3]
# l.push('12') --> there is no push function.

# key error:
# d={'name': 'abrar'}
# print(d['age'])  --> age is not in dictionary.
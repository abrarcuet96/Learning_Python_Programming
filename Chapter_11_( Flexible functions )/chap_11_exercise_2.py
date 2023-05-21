# Exercise_02:
# def a function
# names=['abrar','haider']
# make first letter--> capital and print as a list
# print(func(names))
# print(func(names,reverse_str=True))

def func(l,**kwargs):
    if kwargs.get('reverse_str')==True:
        return [name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]
name_list=['abrar','haider']
print(func(name_list))
print(func(name_list, reverse_str=True))
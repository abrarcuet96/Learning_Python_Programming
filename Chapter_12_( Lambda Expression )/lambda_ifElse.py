def func(s):
    if len(s)>5:
        return True
    return False
print(func('abc'))

# Using Lambda:
func1= lambda s: True if len(s)>5 else False
print(func1('abrarhaider'))
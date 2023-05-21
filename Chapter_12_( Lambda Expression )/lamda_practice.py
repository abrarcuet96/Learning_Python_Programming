def is_even(a):
    return a%2==0
print(is_even(4)) #output-->True

# Using Lambda:
isEven=lambda a: a%2==0
print(isEven(4))

def last_char(s):
    return s[-1]
print(last_char('abrar'))

# Using Lambda:
lastChar= lambda s: s[-1]
print(lastChar('Abrar'))
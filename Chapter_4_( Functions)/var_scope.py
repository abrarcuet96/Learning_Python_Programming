a=3 #global variable
def func():
    global a
    x=a #local variable
    return x
print(func()) #will print 3
print(x) #will give error #we cannot print local variable
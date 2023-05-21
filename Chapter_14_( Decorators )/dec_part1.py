def dec_func(any_func):
    def wrapper_func():
        any_func()
        print('This function is great')
    return wrapper_func
def func1():
    print('Hi,it is function 1')
func1=dec_func(func1)
func1()
def func2():
    print('Hi, it is function 2')
func2=dec_func(func2)
func2()

# Or, use @dec_func;
@dec_func
def func1():
    print('Hi,it is function 1')
func1()
@dec_func
def func2():
    print('Hi, it is function 2')
func2()
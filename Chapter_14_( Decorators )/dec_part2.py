def dec_func(any_func):
    def wrapper_func(*args,**kwargs):
        print("This is awesome function")
        return any_func(*args,**kwargs) 
        # to print we have to return the function.
        # args,kwargs is used so that it can take multiple arguments.
    return wrapper_func

@dec_func
def add(a,b):
    return a+b
print(add(2,3))

@dec_func
def func(a):
    print(f"Hi with {a}")
func(5)
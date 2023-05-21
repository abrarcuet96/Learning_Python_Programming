# To print correct document of function.
from functools import wraps
def dec_func(any_func):
    @wraps(any_func)
    def wrapper_func(*args,**kwargs):
        """ this is wrapper function """
        print("This is awesome function")
        return any_func(*args,**kwargs) 
        # to print we have to return the function.
        # args,kwargs is used so that it can take multiple arguments.
    return wrapper_func
@dec_func
def add(a,b):
    """ this is add function """
    return a+b
print(add.__doc__)
print(add.__name__)
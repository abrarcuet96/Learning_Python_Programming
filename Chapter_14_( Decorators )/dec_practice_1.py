from functools import wraps
def print_function_data(any_func):
    @wraps(any_func)
    def wrapper(*args,**kwargs):
        print(f"You are calling {any_func.__name__} function")
        print(f"{any_func.__doc__}")
        return any_func(*args,**kwargs)
    return wrapper
@print_function_data
def add(a,b):
    """this function takes two numbers as arguments and return their sum"""
    return a+b
print(f"The sum is {add(4,5)}")
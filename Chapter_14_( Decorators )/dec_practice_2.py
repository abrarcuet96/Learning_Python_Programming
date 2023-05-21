from functools import wraps
def only_int_allow(any_func):
    @wraps(any_func)
    def wrapper(*args,**kwargs):
        # data_types=[]
        # for arg in args:
        #     data_types.append(type(arg)==int)
        # if all(data_types):
        #     return any_func(*args,**kwargs)
        # else:
        #     return "Invalid input-->only int input is allowed"
        #or,
        if all([type(arg)==int for arg in args]):
            return any_func(*args,**kwargs)
        return "Invalid input-->only int input is allowed"
    return wrapper
@only_int_allow
def add(*args):
    total=0
    for arg in args:
        total+=1
    return total

print(f"summation is {add(1,2,3,4,5,6,7)}")
print(f"{add(1,2,3,4,5,6,7,[1,2,3,4])}")
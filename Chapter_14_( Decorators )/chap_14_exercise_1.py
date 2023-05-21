# @calculate_time
# def func():
#     print("this is function")
# func()
# this function take 3 sec to run
import time
def calc_time(any_func):
    def wrapper(*args,**kwargs):
        t1=time.time()
        returned_value=any_func(*args,**kwargs)
        t2=time.time()
        print(f"this function take {t2-t1} seconds to run")
        return returned_value
    return wrapper
@calc_time
def func(a,b):
    print(f"summation is {a+b}")
    print(f"subtraction is {a-b}")
    print(f"multiplication is {a*b}")
    print(f"division is {a/b}")

func(5,2)
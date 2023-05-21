# Exercise_01:
# define function
# take a list as input
# example:
# nums=[1,2,3]
# output-->to_power(3,*nums) --> list-->[1,8,27]
# if user didn't pass any args then give user a message 'hey you didn't pass args'
# use list comprehension

def to_power(num,*args):
    if args:
        return [i**num for i in args]
    else:
        return "hey you didn't pass args"

num_list=[]
print(to_power(3,*num_list))
# *operator
# *args
## * --> converts all arguments to tuple.
def all_total(*args):
    print(args)
all_total(1,2,3,4,5) # the arguments will covert to a tuple --> (1, 2, 3, 4, 5)

###
def total_num(*args):
    total=0
    for num in args:
        total+=num
    return total
print(total_num(1,2,3)) #--> that's mean, now we can pass any number of argument in that function.
print(total_num(1,2,3,4,5))
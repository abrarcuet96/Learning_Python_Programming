def multiply_nums(num1,num2,*args):
    multiply=1
    for i in args:
        multiply*=i
    return multiply
print(multiply_nums(2,3,3,4)) 
# Here [2,3 are normal parameters]
# output--> 3x4=12
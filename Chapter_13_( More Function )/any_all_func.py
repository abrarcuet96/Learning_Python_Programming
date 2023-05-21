num1=[2,4,6]
num2=[1,2,3,4,5,6]
evens1=[]
for num in num1:
    evens1.append(num%2==0)
print(evens1)

### all():
print(all([True,True,True])) 
# will find if in evens1 list all is even(True) or not

# Using List comp:
# we can do it in one line.
print(all([num%2==0 for num in num1]))

## any():
print(any([num%2==0 for num in num1]))
print(any([num%2==0 for num in num2])) # if any number is even it will give True
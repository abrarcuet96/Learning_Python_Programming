name="Abrar"
age= 23
# print("Hello " +name+ " your age is " + str(age))
# This syntax looks ugly
# Instead of this we can use python 3  syntax

print("Hello {} your age is {} ".format(name,age)) 
# here we don't need to concern whether the age is in int or string

# Or, we can use python 3.6 syntax

print(f"Hello {name} your age is {age} ") 
# {} are called place holder
# just use f before quotes

# we can do calculation also
print(f"Hello {name} your age is {age+3} ") 
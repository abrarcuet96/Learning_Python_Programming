# Let's try adding two numbers:
# num1=input("enter first number- ")
# num2=input("enter second number- ")
# total= num1+num2
# print("Total is = "+ total) --> it will not give correct result as the numbers are treated as string

# we have to use int() function
num1=int(input("enter first number- "))
num2=int(input("enter second number- "))
total= num1+num2
print("TOtal is "+ str(total)) 
# here total is an integer so we need to convert it to string to add with string

# we can use float() instead of int() to get floating point number

num_1=str(4)
num_2=float(3)
num_3=int(2)
print(num_2+num_3) # we can add integer and float but the result will be in float
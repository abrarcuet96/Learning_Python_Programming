# Find the greater number:
###
def compare(a,b):
    if a>b:
        return "a is greater than b"
    elif a<b:
        return "b is greater than a"
    else:
        return "a and b are equal"

num1=int(input("Enter a: "))
num2=int(input("Enter b: "))

print(compare(num1,num2))

###
def greater(a,b):
    if a>b:
        return a
    else:
        return b
    
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

bigger= greater(num1,num2)
print(f"{bigger} is greater")
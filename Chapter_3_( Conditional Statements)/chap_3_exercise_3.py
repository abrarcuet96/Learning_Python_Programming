# Exercise_03:
# sum of n natural numbers
# ask a user for natural number(n)
# print total from 1 to n

n=int(input("Enter value of n: "))

summ=0
i=1
while i<=n:
    summ+=i
    i+=1
print(f"summation is {summ}")
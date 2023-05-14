# Exercise_04:
# ask user to input a number containing more than one digit
# example 1234
# calculate 1+2+3+4 and print

digit=input("Enter a digit: ")
length=len(digit)
i=0
summ=0
while i<=(length-1):
    summ+=int(digit[i])
    i+=1
print(f"Summation is {summ}")

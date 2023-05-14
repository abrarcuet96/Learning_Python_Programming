# Ask user a number like 1256
# calculate sum of digits: 1+2+5+6

num=input("Enter a number: ")
length=len(num)

total=0
for i in range(0,length):
    char=num[i]
    total+= int(char)
print(total)

# Exercise_04:
# ask a user for name
# example- Abrar Haider
# print count of each words
# output-
# A:1
# b:1
# r:3
# a:2
#  :1
# H:1
# i:1
# d:1
# e:1

# Way_01:
name=input("Enter your name: ")
length=len(name)

i=0
while i<length:
    char=name[i]
    name1=name[i:length]
    name2=name[0:i]
    x=name2.find(char)
    
    if name2=="" or x==-1:
        print(f"{char} : {name1.count(char)}")

    i+=1

# Way_02:
name=input("Enter your name: ")
length=len(name)
temp_var=""
i=0
while i<length:
    if name[i] not in temp_var:
        temp_var +=name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i+=1
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

name= input("Enter your name: ")

temp="" 
for i in range(0,len(name)):
    if name[i] not in temp:
        temp+=name[i]
        print(f"{name[i]} : {name.count(name[i])}")

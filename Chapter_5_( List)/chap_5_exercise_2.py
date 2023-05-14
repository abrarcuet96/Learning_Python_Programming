# Exercise_02:
# define a function which will take list as a argument and this function
# will return a reversed list
# examples:
# [1,2,3,4] --- > [4,3, 2,1]
# ['wordi', 'word2'] ---> ['word2', 'wordi']
# Note you simply do this with reverse method or {t-1]
# but try to do this with the help of append and return method

# Way-1:
num=input("Enter list: ").split(",")
list_of_num=list(map(int,num))
def reverse_list(l):
    l.reverse()
    return l
print(reverse_list(list_of_num))

# Way-2:
num=input("Enter list: ").split(",")
list_of_num=list(map(int,num))
def reverse_list(l):
    return l[::-1]
print(reverse_list(list_of_num))

# Way-3:
num=input("Enter list: ").split(",")
list_of_num=list(map(int,num))
def reverse_list(l):
    reversed=[]
    for i in range(len(l)):
        popped=l.pop()
        reversed.append(popped)
    return reversed
print(reverse_list(list_of_num))



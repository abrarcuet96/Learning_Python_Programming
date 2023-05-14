# Exercise_05:
# common elements finder function
# define a functions which take 2 lists as input and return a list
# which contains common elements of both lists

# example:
# input ---> [1,2,5,8], [1,2,7,6]
# output ---> [1,2]

# Way_01:
num1=input("Enter 1st list: ").split(",")
list_of_num1=list(map(int,num1))
num2=input("Enter 2nd list: ").split(",")
list_of_num2=list(map(int,num2))

def common_num(l,w):
    common=[]
    for i in l:
        for j in w:
            if i==j:
                common.append(i)
    return common
print(common_num(list_of_num1,list_of_num2))

# Way_02:
def common_num(l,w):
    common=[]
    for i in l:
        if i in w:
                common.append(i)
    return common
print(common_num(list_of_num1,list_of_num2))
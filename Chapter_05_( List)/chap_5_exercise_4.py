# Exercise_04:
# filter odd even
# define a function
# input
# list ---> [1, 2,3,4,5, 6,7]
# ouput ----> [[1,3,5,7], [2,4,6]]

num=input("Enter list: ").split(",")
list_of_num=list(map(int,num))

def odd_even(l):
    new_list=[]
    odd=[]
    even=[]
    for i in l:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    new_list=[odd]+[even]
    return new_list

print(odd_even(list_of_num))
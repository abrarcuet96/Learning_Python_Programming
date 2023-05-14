# Exercise_06:
# function
# [1,2,3, [1,2], [3,4]] , input
# 2
# type()

def num_of_list(l):
    x=0
    for i in l:
        if type(i)==list:
            x+=1
    return x


number_list=[1,2,3,[2,3],[3,4,5]]
print(num_of_list(number_list))
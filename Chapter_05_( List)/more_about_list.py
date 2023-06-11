# Generate lists with range functions:
num=list(range(1,11))
print(num)

# Something more about Pop Method:
num=list(range(1,11))
popped_item=num.pop()
print(num)
print(popped_item)

# Index Method:
num=list(range(1,11))
position=num.index(4)
print(position)
###
num=[1,2,3,4,5,6,7,8,9]
position=num.index(4)
print(position)
###
num=[1,2,3,4,5,6,7,8,9,1]
position=num.index(1)
print(position) # Just find the first 1
###
num=[1,2,3,4,5,6,7,8,9,1]
position=num.index(1,3) # Will start finding from position 3
print(position) 
###
num=[1,2,3,4,5,6,7,8,9,1]
position=num.index(1,3,10) # Will start finding from position 3 to 9
print(position) 

# Pass list to a function:
num=[1,2,3,4,5,6,7,8,9,1]
def negative_list(list):
    negative=[]
    for i in list:
        negative.append(-i)
    return negative
print(negative_list(num))

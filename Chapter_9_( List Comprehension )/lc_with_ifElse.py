num=[1,2,3,4,5,6,7,8]
# Normal Way:
new_list=[]
for i in num:
    if i%2==0:
        new_list.append(i*2)
    else:
        new_list.append(-i)
print(new_list)

# List comprehension:
new_list2=[i*2 if (i%2==0) else -i for i in num]
print(new_list2)
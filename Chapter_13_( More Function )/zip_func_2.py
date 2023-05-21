# *operator with zip
l=[(1,2),(3,4),(5,6),(7,8)]
print(list(zip(*l)))

# In separate variables.
l1,l2=list(zip(*l))
print(f"l1 : {l1}")
print(f"l2 : {l2}")

##
l1=[1,2,3,4]
l2=[2,4,6,8]
new_list=[]
for pair in zip(l1,l2):
    new_list.append(max(pair))
print(new_list)
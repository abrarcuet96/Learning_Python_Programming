# set --> unordered collection of unique items.
s1={1,2,3} # second brackets are used.
print(s1)
# items can't be repeated. # s={1,2,3,2} [not possible]
# indexing is not possible. # print(s[1]) [not possible]
# Why use set? --> to remove duplicate.
# Let's take a list:
l1=[1,2,3,4,4,4,5,6,7,8,9]
# Covert it into set:
s2=set(l1) 
print(s2) # output: {1, 2, 3, 4, 5, 6, 7, 8, 9}
# remove duplicate from l using set() and convert it into list all together.
l2=[1,2,3,4,4,4,5,6,7,8,9]
print(list(set(l2))) # output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Add items in set:
s3={1,2,3}
s3.add(4)
print(s3)

# Remove items from set:
s4={1,2,3}
s4.remove(3)
print(s4)
# Or, use discard() to not get error if the discard item is not in set.
s5={1,2,3}
s5.discard(4)
print(s5)

# Clear method:
s6={1,2,3}
s6.clear()
print(s6) # set's all items will be cleared

# Copy method:
s7={1,2,3}
s8=s7.copy()
print(s8)

# list and dictionary cannot be stored in set.
# int,float,string can be stored.
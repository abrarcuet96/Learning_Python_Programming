numbers=[1,2,3,4]
# map(function,itterable)

# Find square list.

# Using map function:
def square(a):
    return a**2
squares=list(map(square,numbers)) 
# map function will take numbers from numbers and will put them into square function.
print(squares)

# We can also use lambda in map function.
squares_new=list(map(lambda a:a**2,numbers)) 
print(squares_new)

# But we can do similar thing using list comprehension.
squares2=[i**2 for i in numbers]
print(squares2)

# Or,
new_list=[]
for num in numbers:
    new_list.append(square(num))
print(new_list)

###
names=['abrar','araf','ilham']
print(list(map(len,names)))
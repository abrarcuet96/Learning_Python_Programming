# Looping in tuples:
mixed=(1,2,3,4,5,6)
for i in mixed:
    print(i)

# Tuples with one element:
num=(1,) # have to use comma if there is one element in the tuple.
print(num)
print(type(num))

# Tuple without parenthesis:
guitars='yamaha','baton rouge', 'taylor'
print(type(guitars))

# Tuple unpacking:
names=('abrar','araf','ilham')
names1,names2,names3=(names) #shoild be equal number of variables``
print(names2)

# List inside tuples: 
# but we can change list inside tuples.
names=('abrar',['araf','ilham'])
names[1].pop()
names[1].append('radib')
print(names)

# Functions: min,max,sum
mixed=(1,2,3,4,5,6)
print(max(mixed))
print(min(mixed))
print(sum(mixed))
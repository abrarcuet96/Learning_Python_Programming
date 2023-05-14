# search items in set with 'in' keyword:

s={'a','b','c'}
if 'a' in s:
    print("present")
else:
    print("not present")

# For loop:
for item in s:
    print(item) 

# Union and Intersection:
s1={1,2,3,4}
s2={3,4,5,6}
union_set= s1|s2
print(union_set) #output-->{1, 2, 3, 4, 5, 6}
intersection_set= s1&s2
print(intersection_set) #output-->{3, 4} 
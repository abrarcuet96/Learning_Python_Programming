# Find even numbers.

# Using filter function:
def is_even(a):
    return a%2==0
num=[3,4,5,6,7,8,9]
evens=tuple(filter(is_even,num))
print(evens)

# Using lambda:
evens=tuple(filter(lambda a:a%2==0,num))
print(evens)
# Using for loop:
evens_new=filter(lambda a:a%2==0,num)
for even_num in evens_new:
    print(even_num)
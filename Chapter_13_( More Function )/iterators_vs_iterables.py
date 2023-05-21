# list,tuple,string--> iterables
numbers=[1,2,3,4] # iterables
squares=map(lambda a:a**2,numbers) #iterator
for i in numbers:
    print(i)

# How for loop works?
# iter function
# next function
number_iter= iter(numbers)
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))


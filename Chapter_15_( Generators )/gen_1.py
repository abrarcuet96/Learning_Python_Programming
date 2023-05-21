# generator function

def nums(n):
    for i in range(1,n+1):
        yield i #Or, we can write yield(i)
numbers=nums(10)
for num in numbers:
    print(num)
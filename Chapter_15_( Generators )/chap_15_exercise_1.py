# Exercise_01:
# Even generator.
def even_num(n):
    for i in range(2,n+1,2):
        yield i
evens=even_num(7)

for even in evens:
    print(even)
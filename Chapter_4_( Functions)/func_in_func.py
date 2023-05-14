# Find greatest from three numbers using function:

def greater(a,b):
    if a>b:
        return a
    return b
def greatest(a,b,c):
    bigger=greater(a,b)
    return greater(bigger,c)
print(greatest(100,20,30))
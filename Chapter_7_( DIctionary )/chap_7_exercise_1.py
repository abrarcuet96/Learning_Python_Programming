# Exercise_01:
# # define a function that takes a number(n)
# return a dictionary containing cube of numbers from 1 to n
# example:
# cube_finder (3)
# {1:1, 2:8, 3:27}
num=int(input("Enter a number: "))
def cube_finder(n):
    cube_dict={}
    for i in range(1,n+1):
        cube_dict[i]=i**3
    return cube_dict
print(cube_finder(num))
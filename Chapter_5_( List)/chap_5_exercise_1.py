# Exercise_01:
# define a function which will take list containing numbers as input
# and return list containing square of every elements
# example
# numbers = [1,2,3,4]
# square_list (numbers) ----› return ----> [1,2,9, 16]

num=input("Enter list: ").split(",")
list_of_num=list(map(int,num))
# In this method, you use the map() function to apply the int() 
# function to each string in the list of strings returned by the split() method. 
# Then you convert the resulting map object to a list using the list() function.
print(list_of_num)
def square_list(l):
    square=[]
    for i in l:
        square.append(i**2)
    return square
print(square_list(list_of_num))
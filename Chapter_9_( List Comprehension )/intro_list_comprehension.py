# List Comprehension--> create list in one line.

## Create a list of squares from 1 to 10:
# Normal way:
square1=[]
for i in range(1,11):
    square1.append(i**2)
print(square1)
# Using List Comprehension:
new_square1=[i**2 for i in range(1,11)]
print(new_square1)

## Print negative of given list:
# Normal way:
negative1=[]
for i in range(1,11):
    negative1.append(-i)
print(negative1)
# Using List Comprehension:
new_negative1=[-i for i in range(1,11)]
print(new_negative1)

## Print first letter of names in list:
# Normal way:
names=['Abrar','Araf','Arham']
new_list1=[]
for name in names:
    new_list1.append(name[0])
print(new_list1)
# Using List Comprehension:
new_list2=[name[0] for name in names]
print(new_list2)
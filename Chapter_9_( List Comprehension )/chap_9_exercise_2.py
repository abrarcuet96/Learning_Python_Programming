# Exercise_02:
# num to string
# define a function
# input--> [True, False, [1,2,3],1,1.0,3]
# output--> ['1', '1.0', '3']

list_input=[True, False, [1,2,3],1,1.0,3]
# Normal Way:
new_list1=[]
for i in list_input:
    if type(i)==int or type(i)==float:
        new_list1.append(str(i))
print(new_list1)

# List Comprehension:

def newest_list(l):

    return [str(i) for i in list_input if type(i)==int or type(i)==float ]
print(newest_list(list_input))
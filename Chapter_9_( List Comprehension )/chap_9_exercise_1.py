# Normal way:
l=['abc','tuv','xyz']
def reverse_string1(s):
    l_new1=[]
    for i in l:
        l_new1.append(i[::-1])
    return l_new1
print(reverse_string1(l))

# List_comrehension way:
def reverse_string2(w):
    return [i[::-1] for i in l]
print(reverse_string2(l))
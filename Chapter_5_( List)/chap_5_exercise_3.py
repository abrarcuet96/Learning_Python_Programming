# Exercise_03:
# define a function that take list of words as argument and
# return list with reverse of every element in that list
# example
# ['abc', 'tuv', 'xyz'] ---> ['ba', 'vut', 'zyx']

# Way_01:
words_list=input("Enter your word list: ").split(",")
def func_1(w):
    new_word_list=[]
    for i in range(len(w)):
        popped=w.pop()
        new_word_list.insert(0,popped[::-1])
    return new_word_list
print(func_1(words_list))

# Way_02:
words_list=input("Enter your word list: ").split(",")
def func_2(w):
    new_word_list=[]
    for i in w:
        
        new_word_list.append(i[::-1])
    return new_word_list
print(func_2(words_list))


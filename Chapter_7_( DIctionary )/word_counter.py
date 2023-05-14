## count letters in an alphabet:
# Ex: Abrar Haider--> {'A': 1, 'b': 1, 'r': 3, 'a': 2, ' ': 1, 'H': 1, 'i': 1, 'd': 1, 'e': 1}

def word_counter(s):
    count={}
    for char in s:
        count[char]=s.count(char)
    return count
print(word_counter('Abrar Haider'))
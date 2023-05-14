# Define is_palindrome function that take one word in string as input
# and return True if it is palindrome else return False
# palindrome---> word that reads same backwards as forwards

###
def is_palindrome(name):
    if name==name[::-1]:
        return True
    return False

name=input("Enter a name: ")
print(is_palindrome(name))

###
def is_palindrome(word):
    return word==word[::-1]

word=input("Enter a name: ")
print(is_palindrome(word))
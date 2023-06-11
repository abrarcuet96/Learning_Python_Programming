# This is comment
# For printing string we use single quotes or double quotes
print('hello world')
print("hello world")

# Escape sequence:
# Single quotes can be used in between double quotes viceversa not possible
print("hello\"world\"world")
print('I\'m Abrar')

# Next Line:
print("Line A\nLine B\nLine C")

# Tab:
print("name\tAbrar")

# Use Double \\ to print \ 
# Use Four \\\\ to print \\
print("This is backslash \\")
print("This is double backslash \\\\")

# To eliminate one alphabet
print("Hell\blo")

# Escape sequence as normal text:
print("Line A \\n Line B")
print("Line A \\t Line B")
# Shortcut: use r before first double quote;
print(r"line A \n Line B")

# How to print with backslash:
#\"="
#\\=\
#\\\"=\"

# To output : \" \'
print(" \\\" \\\'  ")

# EXERCISE:01
print("this is \\\\ backslash")
print(r"this is \\ backslash")
# EXERCISE:02
print("these are /\\/\\/\\/\\/\\ mountains")
print(r"these are /\/\/\/\/\ mountains")
# EXERCISE:03
print("he is\tawesome")
# EXERCISE:04
print("\\\" \\n \\t \\\' ")
print(r"\" \n \t \' ")

# Print Emoji:
print("\U0001F602") #CODE FROM unicode.org
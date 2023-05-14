# Exercise_03:
# Take two comma separated inputs from user 
# 1. user's name
# 2. a single character

# output: 2 print lines
# 1. user's name length
# 2. count the character that user inputed 
# --> case insensitive count(capital,small bosth should be counted)

name,char=input("Enter your name and a character: ").split(",")
print(f"User's name length is {len(name)}")
# print(f"The inputed character repeats {name.lower().count(char.lower())} times")
# here everything is converted to lower

# if user put any space while inputting
print(f"The inputed character repeats {name.strip().lower().count(char.strip().lower())} times")

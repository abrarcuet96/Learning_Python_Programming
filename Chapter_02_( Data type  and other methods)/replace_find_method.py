# replace():
name="A b r a r"
print(name.replace(" ",",")) # replace space with comma

string="She is beautiful and she is good teacher"
print(string.replace("is","was",1)) #first one 'is' will be replaced
print(string.replace("is","was",2)) #Both 'is' will be replaced

# find():
# To find the position of character in a string
print(f"The position of first 'is' is {string.find('is')} ")
is_pos1=string.find("is")
is_pos2=is_pos1+1
print(f"The position of second 'is' is {string.find('is',is_pos2)} ")
# To solve space problem we use this method.
name="   A b r a r   "
print(name.lstrip()) #Left side spaces will remove
print(name.rstrip()) #Right side spaces will remove
print(name.strip())  #Left and Right side spaces will remove

# To remove inner spaces:
print(name.replace(" ",""))
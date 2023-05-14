#strings
#collection of characters inside single quotes or double quotes

first_name="Abrar"
last_name="Haider"
full_name=first_name+" "+last_name
print(full_name)

#strings only can be added with strings --> [print(full_name+3)--> not possible]
#possible--> print(full_name+"3")
print(full_name+"3")
#possible--> print(full_name+str(3)) --> [str() = converts to string]
print(full_name+str(3))

print(first_name*3) #first name will print 3 times
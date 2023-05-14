# More than one input in one line using split() function:

name,age=input("Enter your name and age: ").split(",") 

# we can give anything instead of "," in the split() fuction
# but we have to write that thing while giving input
# Like, Enter your name and age: Abrar,23
# Or, if we code: name,age=input("Enter your name and age: ").split("/")
# We have to write: Enter your name and age: Abrar/23

print("Your name is " + name)
print("Your age is " +age)
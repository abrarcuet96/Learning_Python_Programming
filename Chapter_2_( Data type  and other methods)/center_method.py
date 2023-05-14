name="Abrar"
#we want to add two stars in left and right--> **Abrar**
print(name.center(9,"*")) #Abrar=5,2stars+2stars=4; 5+4=9

#Input your name and Add two stars left and right:
name= input("Enter your name: ")
x=len(name)
print(f"Adding two stars left and right {name.center(x+4,'*')}")
# Enter your age and print corresponding ticket price.

age=int(input("Enter age: "))
if age<=0:
    print("Enter correct age")
elif 1<=age<=3:
    print("Ticket is free")
elif 4<=age<=10:
    print("Ticket price: 150tk")
elif 11<=age<=60:
    print("Ticket price: 150tk")
else:
    print("Ticket price: 200tk")
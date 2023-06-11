# Exercise_01:

# Ask user to input 3 numbers,
# and you have to print average of three number using string formatting.
# Try to take all three comma separated inputs in one line.

# NORMAL WAY:
num_1=int(input("Enter 1st Number: "))
num_2=int(input("Enter 2nd Number: "))
num_3=int(input("Enter 3rd Number: "))
avg= (num_1+num_2+num_3)/3
print("The average is "+str(avg))

# Python 3 syntax
num_1,num_2,num_3= input("Enter Three Numbers: ").split(",")
avg= (int(num_1)+int(num_2)+int(num_3))/3
print("The average is {}".format(avg))

#Python 3.6 syntax
num_1,num_2,num_3= input("Enter Three Numbers: ").split(",")
avg= (int(num_1)+int(num_2)+int(num_3))/3
print(f"The average is {avg}")
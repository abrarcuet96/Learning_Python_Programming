# Exercise_02: Watch COCO 

# Ask user's name and age
# If user's name start with ('a' or 'A') and age is above 10 then
# Print 'you can watch coco movie'
# Else print 'sorry, you cannot watch coco'

user_name= input("Enter your name please: ")
user_age= int(input("Enter your age please: "))

first_letter= user_name[0]

if (first_letter=='a' or first_letter=='A')  and user_age>=10:
    print("You can watch COCO")
else:
    print("Sorry, you cannot watch COCO")
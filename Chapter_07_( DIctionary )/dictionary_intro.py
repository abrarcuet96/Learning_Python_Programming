# Why we use dictionaries?
# because lists are not enough to represent real data

# Supppose a list:
user_info=['abrar',23,['pathaan','dhoom','krrish'],['sketching','gardenning','cycling']]
# from the list we cannot exectly about which value means what
# but using dictionary we can do that.

# What are dictionaries?
# Unordered collections of data in key : value pair.

# How to create dictionaries?
user_info1={
    'name':'abrar',
    'age': 23,
    'fav_movies':['pathaan','dhoom','krrish'],
    'hobbies':['sketching','gardenning','cycling']
}
print(user_info1)

# Another method to create dictionary:
user_info2=dict(name='abrar',age=23)
print(user_info2)

# How to access data from dictionary?
user_info3={
    'name':'abrar',
    'age': 23,
    'fav_movies':['pathaan','dhoom','krrish'],
    'hobbies':['sketching','gardenning','cycling']
}
print(user_info3['name'])
print(user_info3['age'])

# A dicionary can store any type of data.

# How to add data to empty dictionary?
user_info4={}
user_info4['name']='mohit'
user_info4['age']= 12
print(user_info4)
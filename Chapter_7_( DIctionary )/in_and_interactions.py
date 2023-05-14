# In keyword:
# searching using key:
user_info={
    'name':'abrar',
    'age': 23,
    'fav_movies':['pathaan','dhoom','krrish'],
    'hobbies':['sketching','gardenning','cycling']
}
if 'name' in user_info:
    print("present")
else:
    print("not present")

# searching using value:
user_info={
    'name':'abrar',
    'age': 23,
    'fav_movies':['pathaan','dhoom','krrish'],
    'hobbies':['sketching','gardenning','cycling']
}
if 'abrar' in user_info.values():
    print("present")
else:
    print("not present")

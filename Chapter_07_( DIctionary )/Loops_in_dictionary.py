# To print all keys:
user_info={
    'name':'abrar',
    'age': 23,
    'fav_movies':['pathaan','dhoom','krrish'],
    'hobbies':['sketching','gardenning','cycling']
}
for i in user_info:
    print(i)

# To print all values:
user_info={
    'name':'abrar',
    'age': 23,
    'fav_movies':['pathaan','dhoom','krrish'],
    'hobbies':['sketching','gardenning','cycling']
}
for i in user_info.values():
    print(i)

# Print values using keys:
user_info={
    'name':'abrar',
    'age': 23,
    'fav_movies':['pathaan','dhoom','krrish'],
    'hobbies':['sketching','gardenning','cycling']
}
for i in user_info:
    print(user_info[i])

# Values Method:
user_info_values=user_info.values()
print(user_info_values)

# Keys Method:
user_info_keys=user_info.keys()
print(user_info_keys)

# Items Method:
user_items= user_info.items()
print(user_items)

for key,value in user_items:
    print(f"key is {key} and value is {value}")
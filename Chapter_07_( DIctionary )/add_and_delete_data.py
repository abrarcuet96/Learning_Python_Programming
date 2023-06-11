user_info={
    'name':'abrar',
    'age': 23,
    'fav_movies':['pathaan','dhoom','krrish'],
    'hobbies':['sketching','gardenning','cycling']
}
# How to add data:
user_info['fav_songs']=['sog1','song2']
print(user_info)

# Pop method:
popped_item=user_info.pop('fav_movies')
print(f"popped item is {popped_item}")
print(user_info)

# Popitem Method:
popped_item=user_info.popitem()
print(f"popped item is {popped_item}")
print(user_info)
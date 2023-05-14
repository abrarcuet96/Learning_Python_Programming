user={}
user['name']=input("Enter your name: ")
user['age']=int(input("Enter your age: "))
user['fav_movies']=input("Enter your fav movies comma separated: ").split(",")
user['fav_songs']=input("Enter your fav songs comma separated: ").split(",")

user_items=user.items()
for key,value in user_items:
    print(f"{key} : {value}")
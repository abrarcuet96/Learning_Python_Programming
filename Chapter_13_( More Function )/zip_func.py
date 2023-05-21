user_id=['user1','user2','user3']
first_names=['abrar','araf','ilham']
last_names=['haider','haider','labib']
print(list(zip(user_id,first_names,last_names)))
# output-->[('user1', 'abrar', 'haider'), ('user2', 'araf', 'haider'), ('user3', 'ilham', 'labib')]
# it can be converted to dictionary but have to use only two list.
print(dict(zip(user_id,first_names)))
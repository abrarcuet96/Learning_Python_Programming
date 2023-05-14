# Fromkeys:
# user={
#     'name':'unknown',
#     'age':'unknown',
#     'country':'unknown',
# }

user= dict.fromkeys(['name','age','country'],'unknown')
print(user)

user= dict.fromkeys(range(1,4),'unknown')
print(user)

user= dict.fromkeys(['name','age','country'],['abrar','haider'])
print(user)

# Get Method:
user= dict.fromkeys(['name','age','country'],'unknown')
print(user)
print(user.get('name'))
# Or,
if user.get('name'):
    print("Present")
else:
    print("Not present")

# Clear Method:
user.clear()
print(user)

# Copy Method:
user= dict.fromkeys(['name','age','country'],'unknown')
user_copy=user.copy() # same but different dictionary
# Or,
user_copy=user # same dictionary
print(user_copy.popitem())
print(user)
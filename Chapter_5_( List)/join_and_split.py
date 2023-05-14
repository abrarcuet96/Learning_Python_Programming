# Split Method:
user_info='harshit 24'.split() # will split from spaces
print(user_info)

###
user_info='harshit,24'.split(",") # will split from spaces
print(user_info)

###
name,age='harshit 24'.split() # will split from spaces
print(name)
print(age)

# Join Method:
user_info=["harshit","24"] #must be in string
print(",".join(user_info))
###
user={
    'name':'abrar',
    'age':23
}
print(user.get('movies')) # If no such key in dictionary it will print 'None'.

# If we want to print anything without None.
print(user.get('movies','not found!'))

### If one key is written more than one:
user={
    'name':'abrar',
    'age':23,
    'age':34
}
print(user) #age will be overwrited with the later one.
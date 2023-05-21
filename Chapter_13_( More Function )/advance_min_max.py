# Find max length name.
names=['abrar','araf','opy']
print(max(names, key= lambda item: len(item)))

# Find min length name.
names=['abrar','araf','opy']
print(min(names, key= lambda item: len(item)))

# Find max according to score.
students=[
    {'name':'abrar','score':20,'age':21},
    {'name':'araf','score':30,'age':18},
    {'name':'aopy','score':10,'age':26}
]
print(max(students, key=lambda item:item.get('score')))
print(max(students, key=lambda item:item.get('score'))['name'])

###
students={
    'abrar':{'score':20,'age':21},
    'araf':{'score':30,'age':18},
    'opy':{'score':10,'age':26}
}
print(max(students,key=lambda item: students[item]['score']))
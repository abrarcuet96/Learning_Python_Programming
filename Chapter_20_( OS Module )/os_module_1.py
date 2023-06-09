import os
# CREATE FOLDER:
# cwd--> current working directory
print(os.getcwd())
# to create a folder in cwd:
# os.mkdir('movies')
# to check wheather a folder exist or not:
# print(os.path.exists('movies'))

# Or, we can use condition:
# if os.path.exists('movies'):
#     print('already exists')
# else:
#     os.mkdir('movies')

# CREATE FILE:
# open('file.txt','a').close()

# to create folder in different location:
# os.mkdir(r'F:\new_location\movies')

# or change directory:
# os.chdir(r'F:\new_location')
# if os.path.exists('movies'):
#     print('already exists')
# else:
#     os.mkdir('movies')

# to know the containing files as a list:
# print(os.listdir())

# to get full path:
# for item in os.listdir():
#     path=os.path.join(os.getcwd(),item)
#     print(path)
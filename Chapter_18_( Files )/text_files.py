# open function: (it opens a text file)
f= open('file1.txt','r')

# read method: (it reads the text)
print(f.read())

# tell method: (it indicate where the cursor is)
print(f'cursor position - {f.tell()}')
print(f.read())
print(f'cursor position - {f.tell()}')

# seek method: (it changes the position of the cursor)
print('before seek method')
print(f'cursor position - {f.tell()}')
print(f.read())
print(f'cursor position - {f.tell()}')
f.seek(7)
print('after seek method')
print(f'cursor position - {f.tell()}')
print(f.read())
print(f'cursor position - {f.tell()}')

# readline method: (it reads one line at a time)
print(f.readline(),end='')
print(f.readline())

# readlines method: (it add all lines in a list)
lines=f.readlines()
print(lines)

## Data discripter:
# To know file names:
print(f.name)

f.close()
# To see wheather the file is closed or not:
print(f.closed)
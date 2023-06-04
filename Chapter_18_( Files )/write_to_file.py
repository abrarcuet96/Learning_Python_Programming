# we can use w/a/r+ :

# w --> when your file is already empty.
# or you don't want to delete your existing data.
with open('file2.txt','w') as f:
    f.write('hello a new file is created')


# a(append)--> write after existing text.
with open('file2.txt','a') as f:
    f.write('\nhello it is a new line')


# r+ --> we can read and write both.
with open('file3.txt','r+') as f:
    f.seek(len(f.read()))
    f.write('\nplease do it')

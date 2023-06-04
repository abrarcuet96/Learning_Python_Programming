# Exercise_01:

# read from file4.txt:
# Abrar,100
# Haider,50
# Araf,200
# Ilham,500

# and, write to file5.txt as follows:
# Abrar's salary is 100
# Haider's salary is 50
# Araf's salary is 200
# Ilham's salary is 500

with open('file4.txt','r') as rf:
    with open('file5.txt','w') as wf:
        for line in rf.readlines():
            name,salary=line.split(',')
            wf.write(f'{name}\'s salary is {salary}')
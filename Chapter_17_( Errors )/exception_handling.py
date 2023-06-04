# try,except:

while True:
    try:
        age=int(input('enter yout age: '))
        break
    except ValueError:
        print('Invalid input, try again ...')
 
if age<18:
    print('you can\'t play this game')
else:
    print('you can play this game')
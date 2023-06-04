# Else, FInally:
while True:
    try:
        age=int(input('enter yout age: '))
        
    except ValueError:
        print('Invalid input, try again ...')
    else:
        print(f"user input {age}")
        break
    finally:
        print("finally blocks ...") # this block will always run.
 
# Condition:
if age<18:
    print('you can\'t play this game')
else:
    print('you can play this game')
# Exercise_01:
# Devision using try and except:
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        print(err)
    except TypeError as err:
        print(err)
    except:
        print('unexpected error')

print(divide(10,2))
print(divide(10,0))
print(divide(10,'2'))
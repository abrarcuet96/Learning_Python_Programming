# kwargs--> keyword arguments
def func(**kwargs):
    print(kwargs)
func(first_name='Abrar', last_name='Haider')
# will print a dictionary

# forloop in kwargs:
def func1(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} : {v}")
func1(first_name='Abrar', last_name='Haider')

# dictionary unpacking:
d={
    'name':'abrar',
    'age': 23
}
func1(**d)
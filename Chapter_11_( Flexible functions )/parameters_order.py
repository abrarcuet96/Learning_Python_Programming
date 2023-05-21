# func(normal_parameter, *args, default_parameters, **kwargs)
def func(name,*args,last_name='unknown',**kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)
func('Abrar',2,3,a=1,b=2)
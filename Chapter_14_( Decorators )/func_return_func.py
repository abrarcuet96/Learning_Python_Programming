def outer_func():
    def inner_func():
        print("inside inner func")
    return inner_func
var=outer_func() #it will return nothing
var() # it will return "inside inner func"

###
def outer_func2(msg):
    def inner_func2():
        print(f"message is {msg}")
    return inner_func2

var=outer_func2("Hello there!!")
var()

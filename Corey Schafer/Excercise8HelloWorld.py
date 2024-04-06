"""
def hello_func():
    print("Hello !!!")

#hello_func()

for i in range(5):
    hello_func()

#DRY - principle 

"""
# positional and KWargs example 

def hello_func(greeting,name="you"):
    return "{} {}".format(greeting,name)

def student(*args,**kwargs):
    print(args)
    print(kwargs)


#print(hello_func("hi"))
student("Math","Arts", name ="Biology", age=55)




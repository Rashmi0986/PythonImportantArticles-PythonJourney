#LEGB rules 
# Local , Enclosed , Global, Built-in 
'''



#Global Scope
X = 'global x'

def test():
    #Y is Local Scope 
    y = 'local y'
    print(y)

test()
print(X)



def test():
    #Y is Local Scope 
    global x
    x = 'local x'
    print(x)

test()
#Please note here x is accessible outside method too as it is global now 
print(x)

#Built-in scope 
import builtins
print(dir(builtins))

m = min([5,3,2,4,1])
print(m)

def test():
    #Y is Local Scope 
    global x
    y = "local y" #Local scope #enclosed scope to method 
    x = 'global x'
    print(y)
    print(x)

test()
print(x) # global Scope accessing outside the method since it's scope is global 


'''

def outer():
    x = "outer x"
    def inner():
        x = 'inner x'
        print(x)
    inner()
    print(x)

outer()






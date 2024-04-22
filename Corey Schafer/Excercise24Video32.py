
"""
class Duck:
    def quack(self):
        print('Quack ,quack ')
    
    def fly(self):
        print('Flap Flap ')
    
class Person:
    def quack(self):
        print('I am Quacking like a duck ')
    
    def fly(self):
        print("I'm flapping my arms")


def quack_and_fly(thing):
    if isinstance(thing , Duck): # is instance 
        thing.quack()
        thing.fly()
    else:
        print("This has to be duck")
    
    print()

def quack_and_fly(thing):
    thing.quack()
    thing.fly()

    


# hasattr example - LBYL - Look before you Leap (non-pythonic way)
def quack_and_fly(thing):
    if hasattr(thing, Duck):
        if callable(thing.quack): # check those methods exist  in that class
            # - James powell technique 
            thing.quack()
    
    if hasattr(thing,Person):
        if callable(thing.quack):
            thing.quack()
        


#Optimal way to solve the above problem - use try catch - Pythonic
def quack_and_fly(thing):
    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as e:
        print(e)
    


d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)


"""

"""
Another example
"""
"""
#LBYL
person = {'name': "Rashmi", "age": 13, "Job": "Programmer"}
if 'name' in person and 'age' in person and 'Job' in person:
    print("Am {name} and I am {age} years old and I am a {Job}".format(**person))
else:
    print("Missing some keys")


#EAFP - Easy to ask for forgiveness than Permission 
try:
    print("Am {name} and I am {age} years old and I am a {Job}".format(**person))
except KeyError as e:
    print("Missing Key {}".format(e))
"""

#with the list s - LBYL -npn pythonic 
my_list = [1,2,3,4,5,6]
"""
if len(my_list) > 6:
    print(my_list[5])
else:
    print("Index out of range Error")
"""
try:
    print(my_list[6])
except IndexError as e:
    print("{}".format(e))








print("Lets practice everything")
print("you\'d need to know about the escape sequences \\ with that do ")
print("\n newlines and \t tabs ")

poem = """
\t Lovely world
with logic so firmly planted 
can\'t disscern \n the needs of love
nor comprehend passion for love
and requires an explanation 
\n\t\t where there is none 
"""
print("*******")
print(poem)
print("*******")

five = 10 - 2 + 3 - 6 
print(f"this should print five {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars =  jelly_beans / 1000
    crates = jars / 100 
    return jelly_beans, jars , crates

start_point = 10000
beans, jars, crates  = secret_formula(start_point)

print("with the starting point {}".format(start_point))
print(f"we would have beans {beans}, jars {jars} , crates {crates}")

start_point = start_point / 10 # float division 

print("we can also do that this way ")
formula = secret_formula(start_point) # unpacking with the list 
#print("we would have beans {}, jars {} , crates {}".format(beans,jars,crates))
print("we would have beans {}, jars {} , crates {}".format(*formula))




      









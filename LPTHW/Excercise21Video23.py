#function can return something 

def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b

def mul(a, b):
    print(f"Multiplying {a} * {b}")
    return a * b

def division(a, b):
    print(f"Dividing {a} // {b}")
    return a // b

print("Lets Do some math with the real functions")
age = add(30, 5)
height = subtract(78, 4)
weight = mul(90, 2)
iq = division(100 , 2)

print(f"age : {age}, height : {height}, weight :{weight}, IQ: {iq}")
print("Here is a puzzle ")

what = add(age , subtract(height, mul(weight,division(iq, 2))))

print(f"The becomes {what}")





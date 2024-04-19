"""
While Loops 


numbers = []

def iterate(iteration,inc):
    i = 0 
    #Mistake ===>. numbers = [] # shouldn't declare here 
    while i < iteration :
        print(f"At the top is {i}\n")
        numbers.append(i)
        i = i + inc
        print("Numbers Now: ",numbers)
        print("\n")
        print(f"At the Bottom is {i}\n")

iterate(6,1)
print("The numbers ")
print(numbers)
for num in numbers:
    print(num)

"""
numbers = []

def iterate(iteration,inc):
    i = 0 
    for i in range(i, iteration):
        print(f"At the top is {i}\n")
        numbers.append(i)

        #i = i + inc
        print("Numbers Now: ",numbers)
        print("\n")
        print(f"At the Bottom is {i}\n")

iterate(6,1)
print("The numbers ")
print(numbers)
for num in numbers:
    print(num)



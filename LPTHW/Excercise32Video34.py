the_count = [1,2,3,4,5]
fruits = ["apple", "oranges", "peers", "apricots"]
change = [1,"pennies",2, "dimes", 3, "quarters"]

for number in the_count:
    print(f"The count is {number}")

for fruit in fruits:
    print(f"fruit of type {fruit}")


for i in range(len(change)):
    print(change[i])

elements = []
for i in range(1, 6):
    print(f"Adding element {i} the list ")
    elements.append(i)

for ele in elements:
    print(f"Element was: {ele}")

elements_with_range = list(range(0,6))

"""
Gotcha - all the sublist has same Id not a
recommended way to initialise it like below

#elements_of_elements = [[]] * 2 #
if i Append the element to the second list , it is also gets added to the first list as well 
https://www.freecodecamp.org/news/list-within-a-list-in-python-initialize-a-nested-list/
"""
elements_of_elements = [[] for i in range(2)]
#made a mistake with 2d array = declared like this [[]*2] which is wrong 
print(len(elements_of_elements))
#print(elements_of_elements[0])
for i in range(1,11):
    if i <= 5:
        print(f"Adding element {i} to the list 0 ")
        elements_of_elements[0].append(i)
        print(elements_of_elements[0])

    else:
        print(f"Adding element {i} to the list 1 ")
        print(elements_of_elements[1])
        elements_of_elements[1].append(i)

print(elements_of_elements)




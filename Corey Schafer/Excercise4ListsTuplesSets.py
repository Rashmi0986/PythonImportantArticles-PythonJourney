Courses = ["History", "Math", "Physics", "CompSci"]
Courses_2 = ["Languages","Geology"]
print(Courses)
print(len(Courses))

print(Courses[0])
print(Courses[-2]) # negative indexes last but one 

print(Courses[0:2]) #slicing produces new list 
print(Courses[:2])

#modifying lists
Courses.append("Arts")
print(Courses)
Courses.insert(2,"Commerce")
print(Courses)
Courses.extend(Courses_2)
print(Courses)
Courses.remove("Math")
print(Courses)
Courses.pop()
print(Courses)
Courses.reverse() # in-place modification
print(Courses)
#new_Courses = reversed(Courses) #  iterators need to use the for loop for this 

Courses.sort() #in-place sort returns a None Object
print(Courses)

print(sorted(Courses,reverse=True)) #returns new list - if we need the reversed values use variables 
print(Courses) # remains unchanged from the line 28 

nums = [1,2,4,3,5]
print(min(nums))
print(max(nums))
print(sum(nums))

print(nums.index(5))

print("Arts" in Courses)
print(6 in nums)

for item in Courses:
    print(item)

course_str = " - ".join(Courses)

new_list = course_str.split(' - ')
print(course_str)
print(new_list)

#Immutable - Tuples 

tuple_1 = ("History", "Biology", "Geology", "Maths")
tuple_2 = tuple_1
#tuple_1[0] = "Arts" # throws an error as it is immutable 
print(tuple_2)

#Sets - Unordered 
mySet = {"Apple", "Banana" , "Carrot", "Orange"}
mySet_2 = {"Apple", "Banana" , "Carrot", "Orange"}
print(mySet)

print("Banana" in mySet)
print(mySet.intersection(mySet))
print(mySet.union(mySet_2))

#List 
emptyList = []
empty_list = list()

# Tuple 
empty_Tuple = ()
empty_tuple_1 = tuple()

#Set
empty_Set = {} # this is incorrect this is a dictionary always use set() to declare it
empty_Set_2 = set()










nums = [1,2,3,4,5,6,7,8,9,10]

mylist = []
for n in nums:
    mylist.append(n)
print(mylist)

for n in nums:
    mylist.append(n*n)
print(mylist)

#using map + lambda 
mappedList  = []
mappedList = list(map(lambda n : n*n, nums))
print(f"mappedList {mappedList}")

testlist = []
for n in nums:
    if n%2 == 0 :
        testlist.append(n)
print(f"testlist {testlist}")

#using filte lambda 
my_list = list(filter(lambda n: n % 2 == 0, nums ))
print(f"filtered list : {my_list}")

#listComprehensions 
listComprehension = [n * n for n in nums]

print(f"listComprehension {listComprehension}")


#Zip operations with dictionary comprehensions 
names = ["a", "b", "c", "d"]
phones = ["555", "777", "888", "999", "101010"]

dictComp = {a:b for a,b in zip(names,phones)}
print(dictComp)



"""
def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result
num = [1,2,3,4,5]
my_nums = square_numbers(num)
print(my_nums)


#using generators
def square_numbers(nums):
    for i in nums:
        yield i*i
    
num = [1,2,3,4,5]
for n in square_numbers(num): #generator call 
    print(n)

my_nums = (x * x for x in [1,2,3,4,5])
print(*my_nums) #perfect usage -learnt today and applied it 
print(list(my_nums)) # wont work in python 3.x
"""

import memory_profiler as mem_profile
import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

#print('Memory (Before): {}Mb'.format(mem_profile.memory_usage_psutil()))
print('Memory (Before): ' + str(mem_profile.memory_usage()) + 'MB' )

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person

t1 = time.time()
people = people_list(1000000)
t2 = time.time()

print('Memory (After) : {}Mb'.format(mem_profile.memory_usage()))
print('Took {} Seconds'.format(t2-t1))

t1 = time.time()
people = people_generator(1000000)
t2 = time.time()

print('Memory (After) : {}Mb'.format(mem_profile.memory_usage()))
print('Took {} Seconds'.format(t2-t1))

"""
Arithmetic Operators 
Addition 3+2
Subtraction 3 - 2
Division 3//2
Modulo 3 % 2
Exponent 3 ** 2
Multiplication 3 * 2
"""
# rule followed to evealuate the expression is PEMDAS  Exponent , Multiplication , Division , Addition, Subtraction 


print(3**2 + 1)
print(3+2)
print(3-2)
print(3//2)
print(3%2)
print(3*2)

num = 2 
num += 1 #incremental operation 
num *= 1 #multiplication shortcut operation
num //= 1 #Division Shortcut operation

print(round(3.75),1)


#Comparisions 
"""
Equal 3==2
Not Equal 3!=2
Greater Than 3 > 2
Lesser Than 3 < 2
Greater or Equal 3 >= 2
Lesser or Equal 3 <= 2

"""

num_1 = 5 #0101
num_2 = 10 #1010

print(num_1 == num_2)
print(num_1 != num_2)

print(num_1 > num_2)
print(num_2 < num_2)

print(num_1 >= num_2)
print(num_2 <= num_2)

"""
Logical Operations 
num_1 = 2  0010 
num_2 = 3  0011


num_1 and num_2
num_1 or num_2
not num1

"""
#Logical operations
print(num_1 and num_2)
print(num_1 or num_2)
print(not num_1)

#Bitwise Operations 
print(num_1 ^ num_2)
print(num_1 & num_2)
print(num_1 | num_2)


"""
Noticed : if I have performed the AND operation I have got the Largest Number 
if I perform Logical OR i have got the smaller number , 

num_1 = 5 #0101
num_2 = 10 #1010

num_1 and num_2 ==> 10 =======> bigger number 
num_1 or num_2 ==> 5 ==== Smaller number

Discovery = I can use the Logical and or OR operation to 
find the biggest and smallest number in the Array 

"""
# verified with teh list of Numbers too . 
nums = [1,2,3,4,5,6,8]
res = 1
for n in nums:
    #res = res and n =====> Largest Number 
    res = res or n #=====> Smallest number 
print(res)






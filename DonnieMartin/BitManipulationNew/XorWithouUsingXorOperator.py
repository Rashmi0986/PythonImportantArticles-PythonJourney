#Function to find XOR of two numbers without using XOR operator
def findBits(x, y):
    return (x | y) - (x & y)
 
 
if __name__ == '__main__':
 
    x = 65
    y = 80
 
    print('The first number in binary is', bin((x | y)))
    print('The second number in binary is', bin((x & y)))
 
    print('\nXOR is', bin(findBits(x, y)))

#Bit manipulation problems
#https://medium.com/techie-delight/bit-manipulation-interview-questions-and-practice-problems-27c0e71412e7
"""
Constraints:
1 Can we assume just number ?
    Yes
2. Can we assume negative Number or 0?
    Yes
3. Does number fit into memory ?
    Yes
4. Return value ?
    even or odd as string

Testcases:
    0 -> number should't be negative or 0
    5 -> Odd
    6 --> Even
    -1 --> number should't be negative or 0

Algorithm:
    Steps:
    1. num should be logically and with the 1 if we get the
        result zero then it is even
        Else Other wise Odd

Code:
def evenOdd(num):
    if num<=0:
        raise("number should't be negative or 0")
    if (num & 1):
        print("Odd")
    else:
        print("Even")

UnitTests: 
    written below 

"""
#import Exception

class evenOdd:
    def even_Odd(self, num):
        if num<=0:
            raise ValueError("number should't be negative or 0")
        if (num & 1) != 0:
            return "Odd"
        else:
            return "Even"

import unittest

class TestEvenOdd(unittest.TestCase):
    def test_evenOdd(self, func):
        #self.assertEqual(func(-1), "number should't be negative or 0")
        self.assertEqual(func(5),"Odd")
        self.assertEqual(func(6),"Even")
        #self.assertEqual(func(0), "number should't be negative or 0")
        print('Success: test_eveOdd')


def main():
    test = TestEvenOdd()
    even_Odd_Obj = evenOdd()
    test.test_evenOdd(even_Odd_Obj.even_Odd)
    #test.test_evenOdd(even_Odd_Obj.even_Odd(0))

if __name__ == '__main__': #must avoid enclosing __name__ with single quotes
    main()


        

        


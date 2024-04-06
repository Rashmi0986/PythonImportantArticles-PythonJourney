def test_bit_set(number, index):
    '''
    Returns True if number has the index'th bit set
    and False otherwise.
    '''
    mask = 1 << index
    return number & mask != 0

"""
8421
3210 -- bits index
0101  -- number 5
0010  --- index 
0100.  ---Mask left shift of 2 1<<index = 4
0100 = 2nd bit set 
"""
print(test_bit_set(5,2))
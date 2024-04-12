#return the index of the Sublist having maxSum 

def indexofRowWithMaxSum(nums):
    s = 0 
    res = []
    for i, row in enumerate(nums):
        res = sum(row)
        if res > s:
            s = res
            ind = i 
    return [ind, s]

print(indexofRowWithMaxSum([[1,2,3],[4,5,6]]))




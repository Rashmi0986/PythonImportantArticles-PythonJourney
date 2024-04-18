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


"""
#Time complexity of the above solution is O(N2) - quadratic time complexity 
need to reduce it to - Liner time - Think trhough the algorithm . 
Ref for algo time complexity - https://stackoverflow.com/questions/4317414/polynomial-time-and-exponential-time
"""





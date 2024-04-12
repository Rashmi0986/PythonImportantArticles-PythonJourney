#return the index of the Sublist having max ele 


def indexofRowWithMaxEle(nums):
    s = float('-inf')
    res = 0
    ind = 0 
    for i, row in enumerate(nums):
        res = max(row)
        if res > s:
            s = res
            ind = i 
    return [ind, s]

print(indexofRowWithMaxEle([[1,2,3],[4,5,6]]))

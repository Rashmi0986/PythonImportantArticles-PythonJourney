#return the index of the Sublist having min ele 


def indexofRowWithMinEle(nums):
    s = float('inf')
    res = 0
    ind = 0 
    for i, row in enumerate(nums):
        res = min(row)
        if res < s:
            s = res
            ind = i 
    return [ind, s]

print(indexofRowWithMinEle([[1,2,3],[4,5,6]]))

import sys

def radix_sort(arr):
    if not arr:
        return None
    if len(arr) < 2:
        return arr
    
    for i in arr:
        pass


def findMax(arr):
    res = -sys.maxsize
    for i in arr:
        res = max(res, i)
    return res


arr = [0,5,10,3,8,4,7,9,1, 0.5, -3,-10, -100, 2, 6]
print(findMax(arr))

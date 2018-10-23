
def getMaxRob(arr, start, map):
    if  map[start] != -1:
        return map[start]

    if not arr:
        raise ValueError('Array not provided')
    
    end = len(arr) - 1
    if end == start:
        return arr[0]
    
    if end - start == 1:
        return max(arr[start], arr[end])
    
    val = arr[start]
    maxWithStart = val +  getMaxRob(arr, start + 2, map)
    maxWithoutStart = getMaxRob(arr, start + 1, map)

    res = max(maxWithoutStart, maxWithStart)

    if map[start] == -1:
        map[start] = res

    return res



def rob(arr):
    store = [-1] * len(arr) 
    return getMaxRob(arr, 0, store)


arr =[10, 40, 30, 20]
print(rob(arr))
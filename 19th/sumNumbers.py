def sumNumber(array, target):
    if not array:
        return None
    if not target:
        return None
    
    map = {}
    for i in array:
        val = target - i
        if val in map:
            return [val, i]
        map[i] = i
    return None


        


arr = [2, 7, 11, 15]
target = 8
print(sumNumber(arr, target))

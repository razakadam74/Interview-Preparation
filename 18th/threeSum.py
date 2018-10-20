def twoSum(arr, start, target):
    list = []
    map = {}

    for i in range(start, len(arr)):
        lookup = target - arr[i]
        if lookup in map:
            res = [lookup, arr[i]]
            
            if res not in list:
                list.append(res)
        else:
            map[arr[i]] = '0'
    return list

def threeSum(arr):
    if not arr:
        return None
    size = len(arr)
    if size < 3:
        return None
    
    result = []
    for i in range(0, size - 2):
        num = arr[i]
        twoSums = twoSum(arr, i + 1, -num)
        if twoSums:
            for r in range(len(twoSums)):
                res =[num, twoSums[r][0], twoSums[r][1]]
                res.sort()
                if res not in result:
                    result.append(res)
    return result



print(threeSum([-6, 2, 3, 3]))

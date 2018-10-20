def quicksort(arr):

    if len(arr) < 2:
        return arr
    
    pivot = arr[-1]
    less = 0
    greater = 0
    for i in range(0, len(arr) - 1):
        if arr[i] >= pivot:
            greater += 1
        else:
            swap = arr[i]
            arr[i] = arr[less]
            arr[less] = swap
            less += 1
            greater += 1
    
    arr[i+1] = arr[less]
    arr[less] = pivot

    res = []
    left = quicksort(arr[:less])
    right = quicksort(arr[less + 1:])
    res.extend(left)
    res.append(pivot)
    res.extend(right)
    return res


arr = [0,5,10,3,8,4,7,9,1, 0.5, -3,-10, -100, 2, 6]
print(quicksort(arr))
    
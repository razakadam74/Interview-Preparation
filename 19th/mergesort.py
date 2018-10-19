def merge(left, right):
    max_size = max([left, right], key=len)
    l = 0
    r = 0
    sorted_list = []
    while (l < len(left) and r < len(right)):
        if (left[l] < right[r]):
            sorted_list.append(left[l])
            l += 1
        else:
            sorted_list.append(right[r])
            r += 1
    
    while(l < len(left)):
        sorted_list.append(left[l])
        l += 1
    
    while(r < len(right)):
        sorted_list.append(right[r])
        r += 1
    return sorted_list


def mergesort(arr, start, end):
    if start < end:
        mid = (start + end -1) // 2
        mergesort(arr, start, mid)
        mergesort(arr, mid + 1, end)
        merge(arr[0: mid], arr[mid: end])



arr1 = [0,4,5,7,10,14, 18, 20]
arr2 = [2,4,8,10]

arr = [0,5,32,1,2,34,54,2,1,2,5,3,6]
# print({'output': merge(arr1, arr2)})

mergesort(arr, 0, len(arr))
print(arr)
# print(mergesort(arr, 0, len(arr)))





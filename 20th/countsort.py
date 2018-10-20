def countsort(arr):
    count_arr = [0] * 10

    for i in arr:
        count_arr[i] += 1
    

    for i in range(1, len(count_arr)):
        count_arr[i] = count_arr[i -1] + count_arr[i]

    
    res = [0] * len(arr)

    for i in arr:
        count_arr[i] -= 1
        res[count_arr[i]] = i
    return res



arr = [1,4,1,2,7,5,2]

print(countsort(arr))





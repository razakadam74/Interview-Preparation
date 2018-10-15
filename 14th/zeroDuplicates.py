def zeroDuplications(arr):
    dict = {}
    for idx, val in enumerate(arr):
        if dict.get(str(val)):
            arr[idx] = 0
        else:
            dict[str(val)] = 1
    return arr


print(zeroDuplications([0,1,2,3,1,2,4,6,8]))



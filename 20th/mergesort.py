def mergesort(arr):
    if not arr:
        raise ValueError('Array not provided')
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)


def merge(first, second):
    sorted = []
    f = 0
    s = 0
    while (f < len(first) and s < len(second)):
        if first[f] <= second[s]:
            sorted.append(first[f])
            f +=1
        else:
            sorted.append(second[s])
            s += 1
    
    while f < len(first):
        sorted.append(first[f])
        f += 1

    while s < len(second):
        sorted.append(second[s])
        s += 1
    return sorted


t = [1,2,3,4,5,6]
t2 = [0,2,4.5,10, 11, 13]

arr = [2, 3, 12, 32, 4, 65, 31, 21, -21, 0,4,12,232,-3434,34,343,21]
print(mergesort(arr))

# print(merge(t,t2))

def threeSum(arr):
    l = []
    for idx,val in enumerate(arr):
        for i in range(idx + 1, len(arr)):
            for r in range(i + 1, len(arr)):
                if val + arr[i] + arr[r] == 0:
                    l_new =[]
                    l_new.append(val)
                    l_new.append(arr[i])
                    l_new.append(arr[r])
                    l_new.sort() 
                    if l_new not in l:
                        l.append(l_new)
    return l


arr = [-1, 0, 1, 2, -1, -4,2,321,34,32,2,1,-23,-323,23,1,34,56,-5,-34,-54,-56]
print(threeSum(arr))


def oddNumbers(l, r):
    ls = []
    if l % 2 == 0:
        for i in range(l+1,r+1, 2 ):
            ls.append(i)
    else:
        for i in range(l,r+1, 2 ):
            ls.append(i)
    return ls

print(oddNumbers(2,5))


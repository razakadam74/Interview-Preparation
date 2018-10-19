def oneReplace(first, second):
    different  =False
    for i in range(0, len(first, second)):
        if first[i] != second[i]:
            if different:
                return False
    return True


def oneInsert(first, second):
    idx1 = 0
    idx2 = 0
    
    while idx1 < len(first) and idx2 < len(second):
        if first[idx1] != second[idx2]:
            if idx1 != idx2 : 
                return False
            idx2 +=1
        else:
            idx1 +=  1
            idx2 += 2
    return True


def oneAway(first, second):
    if first == second:
        return True
    len_of_first = len(first)
    len_of_second = len(second)
    if len_of_first == len_of_second:
        return oneReplace(first, second)
    elif len_of_first + 1 == len_of_second:
        return oneInsert(first, second)
    elif len_of_second + 1 == len_of_first:
        return oneInsert(second, first)

    return False




print(oneAway('ghana', 'ghanaa'))
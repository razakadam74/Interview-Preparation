def binarySearchRecursion(search_list, search_term):
    if not search_list:
        return False
    if len(search_list) == 1:
        return search_list[0] == search_term
    else: 
        mid = len(search_list) // 2
        print(search_list)
        if (search_list[mid] > search_term):
            return binarySearchRecursion(search_list[0: mid], search_term)
        elif search_list[mid] < search_term:
            return binarySearchRecursion(search_list[mid:len(search_list)], search_term)
        else:
            return True


def binarySearchIterative2(list, term):
    s = 0 
    e = len(list) - 1
    while(s <= e):
        mid = (s + e) // 2
        if list[mid] > term:
            e = mid - 1
        elif list[mid] < term:
            s = mid + 1
        else:
            return mid
    return -1


def binarySearchIterative(list, term):
    if len(list) == 1:
        return list[0] == term
    else:
        s = 0
        l = len(list)
        while (s < l):
            mid = (s + l) // 2
            if list[mid] == term:
                return True
            elif list[mid] > term:
                l = mid
            else:
                s = mid
            print(list[s:l])
        return False


# print(binarySearchRecursion([1,2,3,4,5,6,7,8,9,10], 55))


print(binarySearchIterative2([1,2,3,4,5,6,7,8,9,10], 6))
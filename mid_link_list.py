def findMidNode(linkedList):
    if not linkedList.head
        return None
    else:
        mid = linkedList.head
        index = 0
        while(mid.next):
            index += 1
            if index % 2 == 1:
                mid = mid.next
        return mid


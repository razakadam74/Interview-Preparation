

def removeDuplicateAndSort(word):
    s = {}
    for i in word:
        s[i] = i
    return s.values()

print(removeDuplicateAndSort('geeksforgeeks'))



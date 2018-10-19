def longestString(string):
    prev = {}
    curr = {}

    size = len(string) 
    for i in range(0, size -1):
        curr = {}
        while( i < size -1):
            if string[i] in curr:
                prev = max([prev, curr], key= len)
                curr = {}
            else:
                curr[string[i]] = '0'
            i+=1
    return len(max([prev, curr], key=len))


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    prev = {}
    curr = {}
    size = len(s) 
    for i in range(0, size -1):
        curr = {}
        while( i < size):
            if s[i] in curr:
                prev = max([prev, curr], key= len)
            else:
                curr[s[i]] = '0'
            i+=1
        prev = max([prev, curr], key=len)
    if len(prev) > len(curr):
        print({'prev': prev})
        return len(prev)
    else:
        print({'curr': curr})
        return len(curr)

def lengthOfLongestSubstringBetter(string):
    if not string:
        return -1
    size = len(string)
    l = r = res = 0
    map = set()
    while(l < size and r < size):
        if not map.intersection(string[r]):
            map.add(string[r])
            r += 1
            res = max([res, r -l])
        else:
            map.remove(string[l])
            l += 1
    print(map)
    return res


print(lengthOfLongestSubstringBetter('pwwkew'))

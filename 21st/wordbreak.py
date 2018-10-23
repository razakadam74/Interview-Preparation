def checkIfWord(word, words):
    return word in words 

def wordBreak(string, words):
    i = 0
    r = 1
    while r < len(string):
        if checkIfWord(string[i: r], words):
            i = r
            r + 1
        else:
            r += 1
    return checkIfWord(string[i:r], words)


# string = 'salmonenjoy'
# words =  { 'pear', 'salmon', 'foot', 'prints', 'footprints', 'leave', 'you', 'sun', 'girl', 'enjoy' }

string = 'cars'
words = {'cars', 'ca', 'rs'}
d = dict([[r,i] for i,r in enumerate(words)])


print(wordBreak(string, d))




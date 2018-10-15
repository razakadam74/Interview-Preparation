def longestString(line):
    words = line.split(' ')
    longest_idx = 0
    size = len(words[0])
    for i in range(1, len(words)):
        if (len(words[i]) > size):
            size = len(words[i])
            longest_idx = i
    return words[longest_idx]

def longestWords(line):
    words = words = line.split(' ')
    longest_word = ''
    return max(words, key=len)

word = longestWords('Here is the technical interview study guide. If you have problems logging in to view it, please try a different email address. Thank you and good luck in your interviews!')
print(word)
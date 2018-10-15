from itertools import groupby


def compress_string ( data):
    count = 1
    compress = []
    for i in range(0, len(data) - 1):
        if data[i] == data[i + 1]:
            count +=1
        else:
            compress.append(data[i] + str(count))
            count = 1

    compress.append(data[i+1]+ str(count))
    return min([''.join(compress), data], key=len)


str1 = 'aabcccccaaa'
str2 = 'aaaaabbccbcaabb'


print(compress_string(str2))
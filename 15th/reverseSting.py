      

def reverse(string):
    size = len(string)
    last = size - 1
    new_string = list(string)
    for i in range(0, size / 2):
        c = string[i]
        new_string[i] = string[last - i]
        new_string[last - i] = c

    return ''.join(new_string)


def reverse2(str):
    size = len(str)
    last = size - 1
    list_of_chars = list(str)
    for i in range(0, size/2):
        c = list_of_chars[i]
        list_of_chars[i] = str[last - i]
        list_of_chars[last - i] = c
    return ''.join(list_of_chars)


def multiplicationTable(max):
    for i in range(1, max):
        for r in range(1, max):
            print('%4d' % (i * r), end=" ")
        print()


def readInputFromFile(filename):
    try:
        with open(filename, 'r') as f:
            sum = 0
            for line in f:
                sum += int(line)
            return sum
    except FileNotFoundError as err:
        return err

def findMax(arr):
    return max(arr)




print(findMax([1,24,45,23324,-5353]))
# print(readInputFromFile('inputs'))


# print(multiplicationTable(12))
# print(reverse2('I am Abdul-Razak Adam'))

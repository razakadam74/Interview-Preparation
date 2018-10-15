def reverseString(string):
    new_string = ''
    temp_string = ''
    for i in string:
        if i == ' ':
            new_string += ' '
        else:            
            new_string += '*'
            temp_string += i
            
    returnString = ''
    r= len(temp_string) - 1
    for i in range(len(new_string)):
        if new_string[i] == ' ':
            returnString += ' '
        else:
            returnString += temp_string[r]
            r -= 1
    return returnString


print(reverseString("Help others"))
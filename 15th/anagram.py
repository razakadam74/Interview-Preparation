def checkIfAnagram(string1, string2):

    if not string1 or not string2:
        return False
    string1 = string1.replace(' ', '').lower()
    string2 = string2.replace(' ', '').lower()

    if len(string1) != len(string2):
        return False

    alphabets = 'abcdefghijklmnopqrstuvwxyz'

    dict1 = dict.fromkeys(alphabets, 0)
    dict2 = dict.fromkeys(alphabets, 0)

    for i in range(0, len(string1)):
        dict1[string1[i]] += 1
        dict2[string2[i]] += 1

    return dict1 == dict2


str1 = 'gahann a'
str2 = 'nnahaga'


print(checkIfAnagram(str1, str2))


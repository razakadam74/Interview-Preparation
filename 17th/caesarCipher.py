
from timeit import Timer


def checkCase(c):
    return c.isupper()


def checkIfAlphabet(c):
    return c.isalpha()


'''
A = [65 - 90]  A-Z
B = [97 - 122] a - z
C = [91 - 100] 0- 9
'''


def caesarCipher(string, shifts):
    if not string:
        return ''
    else:
        encripted = []
        for c in string:
            if checkIfAlphabet(c):
                if checkCase(c):
                    encripted.append(chr((ord(c) + shifts - 65) % 26 + 65))
                else:
                    encripted.append(chr((ord(c) + shifts - 97) % 26 + 97))
            else:
                if c.isdigit():
                    encripted.append(str((int(c) + shifts) % 9))
                else:
                    encripted.append(c)
        return ''.join(encripted)


def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


def CaesarCipherBetter(input):
    if not input:
        raise ValueError('Inapporiate Argument value - Empty input')

    if ':' not in input:
        raise ValueError('Inapporiate Argument value - Colon not provided')

    splits = input.split(':', 1)

    shift = splits[0]
    if not shift:
        raise ValueError('Inapporiate Argument value - No shift provided')

    if not is_digit(shift):
        raise ValueError(
            'Inapporiate Argument value -  Shift can be only numbers')
    else:
        shift = int(shift)
        if shift < -1000000000 or shift > 1000000000:
            raise ValueError(
                'Inapporiate Argument value -  Shift can only be within this range -1000000000 and 1000000000 inclusive')

    string = splits[1]
    if not string:
        raise ValueError(
            'Inapporiate Argument value - Text to encrypt is empty')

    if len(string) > 1000000:
        raise ValueError('Inapporiate Argument value - Text is too long')

    encripted = []
    for c in string:
        if checkIfAlphabet(c):
            if checkCase(c):
                encripted.append(chr((ord(c) + shift - 65) % 26 + 65))
            else:
                encripted.append(chr((ord(c) + shift - 97) % 26 + 97))
        else:
            if c.isdigit():
                encripted.append(str((int(c) + shift) % 9))
            else:
                encripted.append(c)
    return ''.join(encripted)


# try:

#     input = '50:dGeSBZO01xKhuB3lhAhdIbqPoIp1OiOOSQbhPayjY6gE79EIzrLGOympTi8ibWtWDO2jCKJjh0o0D3yF3xY1bzdCaMAZzh7tDbvWQ4n1Rl6kJVyBvl51PQCech8oTyubjQabTnuqm0t10o62KYJdfexrPha9ll2WvOLJlPUYUQ2G3j93nAnrWtZZqopgrOqdFWbJSp9e0CN1GDHGiiJJ7pi2J1ylmMcPE8PChmMpoG7DQ1wECE1iXBTiEojKXBsmo8YT5hqLtPvn2YlA49W1UP7Hv3HlMbhTvMfg2UNsKoXSP8CXe0VrkxB6lVbXVspUCFydX9gPJJeyKwwiXesN5mwhvoPl3QWJaRMYJtPq7aZHYj4eT9xvYsilfLju4BnSb2vAZKDPBAtwRKXf8Jfz9VkH6nm1D18MNAA5JJxUNveDQ9uI35i4sUduHaOt5rGK2MCiPXRWN07DZ3J8KM24emouY0lftHU7NUPwvMTCTnGDQ5oL9eSVuX18sUUgFJnv9u9wp33QlffA2pykHSbGhmNxXje8atYhe1H0e14HcBt0rLq8qUVyrNT8EWKKeeWvdcmlU9YPd8vJxmUzlJfitorduOXWuR5pH5eqvMtJtCSGKZxOqvP4h1Z1T0wQCKIf0pnPWMe8yRWXLt5SOmyyTKm2E4Hca8P3WCdvRbsq7LQHAPN2oiTqthe3KUu7BIsOgj0mHuoHvMUtpiWnwHWpOS8MKzPD7y1B8jVhyO92AunBF6fFabA6Nj8vT5hllufk6Us6ykYjsBaspcNdCDqJaBHYa70oCFatdnsgBydQCLLH4e8G7yR360O5VNePKbCfr1YdxRuZHDO24lY2qmB6EnM1ONFLNeSw0RLRR0YUYCUEmTcr50HYre5XRkJ1R7RqkZDf5QJw57qLYc5QvqxVlz4AuJIsFncIM7hF4DdCiPrrZ0LIo18daNvMHL2kApHu4gSw9QwM7lFqnkNSHUrDOjuZQhwe7rui7McLR0dC'

#     encrypted_txt = CaesarCipherBetter(input)
#     print({'output1': encrypted_txt})


# except ValueError as err:
#     print(err)


# print(caesarCipher(':ATTACKATONCEaa02381sdd;./.;sda122', 4))

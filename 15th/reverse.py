def reverse(number):
    result = 0
    while(number != 0):
        val = number % 10
        result = (result*10) + val
        number = number // 10
    return result


print(reverse(1234))

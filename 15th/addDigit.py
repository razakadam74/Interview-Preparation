def addDigit(num):
    while num >= 10:
        num = sum(getDigits(num))
    return num

def getDigits(num):
    s = str(num)
    return [int(i) for i in list(s)]


def betterSolution(num):
    if num < 10:
        return num
    else :
        sum = 0
        while num != 0:
            sum +=  num % 10
            num = num // 10
        return betterSolution(sum)

def iterativeSolution(num):
    while num >= 10:
        num =sum([int(x) for x in list(str(num))])
    return num


def bestSolution(num):
    res = 0
    if num:
        res = 9 if num % 9 == 0 else num % 9  
    return res


#print(addDigit(38))
#print(betterSolution(38))
num = 0
print(iterativeSolution(num))
print(betterSolution(num))
print(bestSolution(num))

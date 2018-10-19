def isPrime(num):
    x = 2
    while(x * x < num):
        if (num % x == 0):
            return False
        x += 1
    return True


print(isPrime(15))
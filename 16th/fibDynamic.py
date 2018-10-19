def allFib(n):
    list = [0] * (n+ 1)
    val = fib(n, list)
    print(val)


def fib(n, memo):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        if memo[n] > 0: return memo[n]
        else:  
            memo[n] = fib(n - 1, memo) + fib(n -2, memo)
            return memo[n]

allFib(100)
# method 1
def fibonacci1(n):
    def fibo_liter(n, x, y):
        if n == 0:
            return x
        else:
            return fibo_liter(n-1, y, x+y)
    return fibo_liter(n, 0, 1)


# method 2
def fibonacci2(n):
    numlist = [0, 1]
    for i in range(n - 2):
        numlist.append(numlist[-2] + numlist[-1])
    return numlist


# method 3
def fibonacci3(n):
    x, y = 0, 1
    while(n):
        x, y, n = y, x+y, n - 1
    return x


"""
def memoized(f):
    cache = {}
    def wrapped(k):
        v = cache.get(k)
        if v is None:
            v = cache[k] = f(k)
        return v
    return wrapped

@memoized
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
"""

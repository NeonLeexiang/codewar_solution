from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    for x in range(2, int(sqrt(n)) + 1):
        if n % x == 0:
            return False
    return True


def judge_number(n):
    for c in str(n):
        if c not in "2357":
            return False
    return True


def not_primes(a, b):
    rl = []
    for i in range(a, b):
        if judge_number(i) and not is_prime(i):
            rl.append(i)
    return rl


"""
ok = {i for i in range(22, 7778)
      if set(str(i)) <= set('2357')
      and not all(i%d for d in range(2, i))}

def not_primes(*a):
    return sorted(set(range(*a)) & ok)
"""


"""
from bisect import bisect_left as bisect

base, n = set("2357"), 20000
sieve = [1,0]*((n>>1)+1)
sieve[2] = 0
for i in range(3, n+1, 2):
    if not sieve[i]:
        for j in range(i**2, n+1, i): sieve[j] = 1

NOT_PRIMES = [x for x in range(n) if sieve[x] and not (set(str(x))-base)]

def not_primes(a, b):
    end = bisect(NOT_PRIMES, b)
    return NOT_PRIMES[bisect(NOT_PRIMES, a, 0, end): end]
"""


"""
from bisect import bisect
from itertools import product
is_prime = lambda n: n % 2 and all(n % x for x in range(3, int(n ** .5) + 1, 2))
prime_digits = (int(''.join(p)) for k in range(2, 6) for p in product('2357', repeat=k))
non_primes = [n for n in prime_digits if not is_prime(n)]
not_primes = lambda a, b: non_primes[bisect(non_primes, a-1): bisect(non_primes, b-1)]
"""

# time out
"""
from math import sqrt


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def judge_number(n):
    for c in str(n):
        if c not in "2357":
            return False
    return True


def not_primes(a, b):
    rl = []
    for i in range(a, b):
        if is_prime(i) is False and judge_number(i):
            rl.append(i)
    return rl
"""


# wrong solution
# time out


"""
from math import sqrt


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def not_primes(a, b):
    number_list = ['2', '3', '5', '7']
    return_list = ['2', '3', '5', '7']
    end_target = 0
    while end_target <= len(str(b)):
        for c in return_list:
            for i in number_list:
                return_list.append(c+i)
        end_target = len(return_list[-1])
    return_list = list(sorted(map(int, return_list)))
    end_list = []
    for c in return_list:
        if a <= c <= b and is_prime(c) is False and c != (2, 3, 5, 7):
            end_list.append(c)
    return end_list
"""


"""
def prime_digits(num):
    primes = [2, 3, 5, 7]
    while num:
        if num % 10 not in primes:
            return False
        num //= 10
    return True 
primes = set([2] + [n for n in range(3, 20000, 2) if all(n % r for r in range(3, int(n ** 0.5) + 1, 2))])
def not_primes(a, b):
    return [i for i in range(a, b) if prime_digits(i) if i not in primes]
"""


"""
p = [n for n in range(10,20000) if set(list(str(n))) <= set(list('2357')) and any(n%p==0 for p in range(2,int(n**0.5)+1))]
def not_primes(a, b): return [n for n in p if n>=a and n<b]
"""


"""
from itertools import product

def isPrime(n):
    return n==2 or n%2 and all(n%p for p in range(3,int(n**.5)+1,2))

def not_primes(a, b):
    low, high = map(len, map(str, (a,b)))
    return [n for d in range(low,high+1) for n in map(int, map(''.join, product("2357",repeat=d))) if a <= n < b and isPrime(n)==False]

"""

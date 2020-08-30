def last_digit(lst):
    if len(lst) == 0:
        return 1
    len_lst = len(lst)
    sum_return = lst[len_lst - 1]

    for i in range(len(lst)-2, 0, -1):
        sum_return = sum_return**lst[i]
    return str(sum_return)[-1]


"""
def last_digit(lst):
    n = 1
    for x in reversed(lst):
        # if use x ** (n % 4 + 4) , it will return false while n = 0
        n = x ** (n if n < 4 else n % 4 + 4) 
    return n % 10
"""


"""
def last_digit(lst):
    if not lst:
        return 1
    else:
        out = 1
        for n in lst[len(lst):0:-1]:
            out = n**out
            if out > 2:
                out -= 2
                out %= 4
                out += 2
    return lst[0]**out% 10
"""


"""
from functools import reduce
        
def last_digit(lst):
    return reduce(lambda p, n: 1 if p == 0 or n == 1 else n if p == 1 or n == 0 else pow(n, p, 40) + 40, lst[::-1], 1) % 10
"""


"""
import functools

def powmod(e, b):
    if e==0 or b==1:
        return 1
    if e==1 or b==0:
        return b
    else:
        return pow(b, e, 20)+20
        

def last_digit(lst):
    return functools.reduce(powmod, lst[::-1], 1) % 10
"""

from functools import reduce


def persistence(n):
    # your code
    numscount = 0
    numlist = map(int, str(n))
    for i in range(10):
        if len(numlist) == 1:
            return numscount
        else:
            n = (reduce(lambda x, y: x * y, numlist))
            numlist = map(int, str(n))
            numscount = numscount+1


"""
def persistence(n):
    nums = [int(x) for x in str(n)]
    sist = 0
    while len(nums) > 1:
        newNum = reduce(lambda x, y: x * y, nums)
        nums = [int(x) for x in str(newNum)]
        sist = sist + 1
    return sist
"""


"""
import operator
def persistence(n):
    i = 0
    while n>=10:
        n=reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i
"""


"""
from operator import mul
def persistence(n):
    return 0 if n<10 else persistence(reduce(mul,[int(i) for i in str(n)],1))+1
"""

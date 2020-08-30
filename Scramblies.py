def scramble(s1, s2):
    #your code here
    count = len(s1)
    for c in s2:
        if c in s1:
            s1 = s1.replace(c, '', 1)
    if count-len(s1) == len(s2):
        return True
    else:
        return False


def scramble(s1, s2):
    #your code here
    s = list(s1+s2)
    for item in list(s2):
        s.remove(item)
    if len(s1)-len(s) <= len(s2):
        return True
    else:
        return False


def scramble(s1, s2):
    s = s1 + s2
    for c in s2:
        s = s.replace(c, '', 2)
    if len(s1)-len(s) == len(s2):
        return True
    else:
        return False


# Python标准库——collections模块的Counter类
"""
from collections import Counter
def scramble(s1,s2):
    # Counter basically creates a dictionary of counts and letters
    # Using set subtraction, we know that if anything is left over,
    # something exists in s2 that doesn't exist in s1
    return len(Counter(s2)- Counter(s1)) == 0
"""



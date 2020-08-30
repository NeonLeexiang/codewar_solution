def solve(s):
    uCount = 0
    lCount = 0
    cCount = 0
    nCount = 0
    for c in s:
        if c.isupper():
            uCount += 1
        elif c.islower():
            lCount += 1
        elif c.isalnum():
            nCount += 1
        else:
            cCount += 1
    return [uCount, lCount, nCount, cCount]


"""
def solve(s):
    res = [0, 0, 0, 0]
    for c in s:
        i = 0 if c.isupper() else 1 if c.islower() else 2 if c.isdigit() else 3
        res[i] += 1
    return res
"""

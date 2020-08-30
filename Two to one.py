def longest(s1, s2):
    # your code
    s1List = list(s1)
    s2List = list(s2)
    longests=s1List+s2List
    longests=list(set(longests))
    longests=sorted(longests)
    longests=''.join(longests)
    return longests


"""
    def longest(a1, a2):
        return "".join(sorted(set(a1 + a2)))
"""


"""
    def longest(s1, s2):
        return ''.join(sorted(set(s1) | set(s2)))
"""

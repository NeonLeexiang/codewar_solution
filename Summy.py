def summy(string_of_ints):
    L = string_of_ints.split(' ')
    sum_of_ints = 0
    for i in L:
        sum_of_ints += int(i)
    return sum_of_ints


"""

# only suitable for python3,can't use sum() in python2 version
def summy(string_of_ints):
    return sum(map(int,string_of_ints.split()))
"""

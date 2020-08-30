def solution(digits):
    diglist = list(digits)
    newlist = []
    for i in range(len(digits)-4):
        newlist.append(int(''.join(digits[i:i+5])))
    return int(''.join(diglist[newlist.index(max(newlist)):newlist.index(max(newlist))+5]))


"""
def solution(dd):
    return max(int(dd[i:i+5]) for i in range(len(dd) - 4))
"""

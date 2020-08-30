"""
 if the strng doesn't have the repeat sum number
"""
def order_weight(strng):
    sList = strng.split(' ')
    sDict = {}
    for i in range(len(sList)):
        a = sum(map(int, sList[i]))
        sDict[sList[i]] = a
    pDict = sorted(sDict.iteritems(), key=lambda d: d[1], reverse=False)
    oList = []
    for i in range(len(pDict)):
        oList.append(pDict[i][0])
    return ' '.join(oList)

"""
can have repeat sum number
"""
def order_weight(strng):
    sList = strng.split(' ')
    s1List = []
    for i in range(len(sList)):
        s1List.append((sum(map(int, sList[i])), sList[i]))
    pDict = sorted(s1List)
    oList = []
    for i in range(len(pDict)):
        oList.append(pDict[i][1])
    return ' '.join(oList)

"""
def order_weight(_str):
    return ' '.join(sorted(sorted(_str.split(' ')), key=lambda x: sum(int(c) for c in x)))
"""

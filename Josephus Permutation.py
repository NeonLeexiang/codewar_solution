def josephus(items,k):
    #your code here
    del_number = k-1
    oList = []
    if len(items) < k and len(items) != 0:
        del_number = del_number % len(items)
        for i in range(len(items)):
            oList.append(items[del_number])
            del items[del_number]
            if len(items) != 0:
                del_number = (del_number + k - 1) % len(items)
            else:
                return oList

    else:
        for i in range(len(items)):
            oList.append(items[del_number])
            del items[del_number]
            if len(items) != 0:
                del_number = (del_number + k - 1) % len(items)
            else:
                return oList
        return oList


"""
def josephus(xs, k):
    i, ys = 0, []
    while len(xs) > 0:
        i = (i + k - 1) % len(xs)
        ys.append(xs.pop(i))
    return ys
"""


"""
def josephus(items,k):
    if len(items)==0: return []
    if len(items)==1: return [items[0]]
    i = ((k-1)%len(items))
    return [items[i]] + josephus(items[i+1:]+items[:i], k)
"""


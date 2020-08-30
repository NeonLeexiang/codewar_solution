def solution(args):
    # your code here
    holdOn = 0
    i = 0
    inset = 0
    outPut = []
    while i < len(args)-1:
        countOn = i
        while args[i]+1 == args[i+1]:
            i += 1
            holdOn += 1
            if i+1 >= len(args):
                break
            else:
                continue
        if i+1 == len(args)-1:
            inset = 1
        if holdOn > 1:
            outPut.append(str(args[countOn])+'-'+str(args[countOn+holdOn]))
            holdOn = 0
            i += 1
            if inset == 1:
                outPut.append(str(args[len(args)-1]))
        elif holdOn == 1:
            outPut.append(str(args[countOn]))
            outPut.append(str(args[countOn+1]))
            i += 1
            holdOn = 0
            if inset == 1:
                outPut.append(str(args[len(args)-1]))
        elif holdOn == 0:
            outPut.append(str(args[countOn]))
            i += 1
            if inset == 1:
                outPut.append(str(args[len(args)-1]))
    return ','.join(outPut)


"""
def solution(args):
    out = []
    beg = end = args[0]
    
    for n in args[1:] + [""]:        
        if n != end + 1:
            if end == beg:
                out.append( str(beg) )
            elif end == beg + 1:
                out.extend( [str(beg), str(end)] )
            else:
                out.append( str(beg) + "-" + str(end) )
            beg = n
        end = n
    
    return ",".join(out)
"""


"""
def solution(args):
    lasts, r = [], []
    for a in args:
        r, lasts = (r + add(map(str, lasts)), [a]) if lasts and lasts[-1] + 1 != a else (r, lasts + [a])
    return ','.join(r + add(map(str, lasts)))
    
add = lambda e: [e[0]] if len(e) == 1 else [e[0], e[1]] if len(e) == 2 else [e[0] + '-' + e[-1]]   
"""

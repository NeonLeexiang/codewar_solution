Alphabet = dict(BINARY='bin',
            OCTAL= 'oct',
            DECIMAL= 'dec',
            HEXA_DECIMAL= 'hex',
            ALPHA_LOWER='allow',
            ALPHA_UPPER='alup',
            ALPHA='alpha',
            ALPHA_NUMERIC='alnum')
def convert(input, source, target):
    """BEGIN"""
    # judge the source
    def judge_source(input, source):
        rinput = input[::-1]
        rdict = dict(allow='abcdefghijklmnopqrstuvwxyz',
                     alup='ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                     alpha='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
                     alnum='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        rdec = 0
        i = 0
        if source == 'bin':
            for num in rinput:
                rdec += int(num) * 2 ** i
                i += 1
            return rdec
        elif source == 'oct':
            for num in rinput:
                rdec += int(num) * 8 ** i
                i += 1
            return rdec
        elif source == 'hex':
            rdec = int(input, 16)
            return rdec
        elif source == 'dec':
            rdec = int(rinput[::-1])
            return rdec
        elif source in rdict:
            rdec = 0
            rl = list(rinput)
            for c in range(len(rl)):
                rdec += rdict[source].index(rl[c]) * len(rdict[source]) ** c
            return rdec
        else:
            return input
    def judge_target(target, rdec):
        rdict = dict(allow='abcdefghijklmnopqrstuvwxyz',
                     alup='ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                     alpha='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
                     alnum='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
                     hex='0123456789abcdef')
        if target == 'bin':
            loutput = ''

            def change(rdec):
                result = '0'
                if rdec == 0:
                    return result
                else:
                    result = change(rdec // 2)
                    return result + str(rdec % 2)
            loutput = str(int(change(rdec)))
            return loutput
        elif target == 'oct':
            loutput = ''

            def change(rdec):
                result = '0'
                if rdec == 0:
                    return result
                else:
                    result = change(rdec // 8)
                    return result + str(rdec % 8)

            loutput = str(int(change(rdec)))
            return loutput
        elif target == 'hex':
            rdict = dict(hex='0123456789abcdef')
            loutput = ''

            def change(rdec):
                result = '0'
                if rdec == 0:
                    return result
                else:
                    result = change(rdec // 16)
                    return result + str(rdec % 16)

            rset = str(int(change(rdec)))
            if int(rset) <= 16:
                loutput = list(rdict['hex'])[int(rset)]
            else:
                for c in rset:
                    loutput += list(rdict['hex'])[int(c)]
                loutput = ''.join(loutput)
            return loutput

        elif target == 'dec':
            return str(rdec)
        elif target in rdict:
            loutput = ''

            def change(rdec):
                rset = []
                if rdec == 0:
                    return rset == [0]
                else:
                    while (rdec != 0):
                        rset.append(rdec % len(rdict[target]))
                        rdec = rdec // len(rdict[target])
                return rset
            rlist = list(change(rdec))
            for item in rlist:
                loutput += list(rdict[target])[item]
            loutput = ''.join(loutput)
            loutput = loutput[::-1]
            return loutput
        else:
            return input


    return judge_target(target,judge_source(input,source))


"""
def convert(input, source, target):
    base_in = len(source)
    base_out = len(target)
    acc = 0
    out = ''
    for d in input:
        acc *= base_in
        acc += source.index(d)
    while acc != 0:
        d = target[acc % base_out]
        acc = acc / base_out
        out = d + out
    return out if out else target[0] 

"""

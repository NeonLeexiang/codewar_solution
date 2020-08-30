from __future__ import division


def sum_of_squares(n):
    import math
    def sos1(n):
        out = []
        m = n
        while sum(out) < n:
            if math.sqrt(m).is_integer():
                out.append(m)
                break
            elif math.sqrt(m) > math.sqrt(3):
                out.append(int(math.sqrt(m)))
                m = m - int(math.sqrt(m)) ** 2
            elif m == 3:
                out += [1, 1, 1]
                break
            elif 1 < math.sqrt(m) < 1.5:
                out += [1, 1]
                break
            elif m == 1:
                out.append(m)
                break
        return out
    def sos2(n):
        out = []
        m = n
        while sum(out) < n:
            if math.sqrt(m).is_integer():
                out.append(m)
                break
            elif math.sqrt(m/2).is_integer():
                out += [m/2, m/2]
                break
            elif m - 2*int(math.sqrt(m/2))**2 >= 1:
                out += [int(math.sqrt(m/2)), int(math.sqrt(m/2))]
                m = m - 2*int(math.sqrt(m/2))**2
                if m == 3:
                    out += [1, 1, 1]
                    break
                elif m == 2:
                    out += [1, 1]
                    break
                elif m == 1:
                    out.append(1)
                    break
        return out
    if n < 18:
        return len(sos1(n))
    elif n >= 18:
        if n - 2*int(math.sqrt(n/2))**2 < 4:
            return len(sos2(n))
        else:
            return len(sos1(n))

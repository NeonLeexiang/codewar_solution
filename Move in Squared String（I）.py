def vert_mirror(strng):
    strng = strng.split('\n')
    for i in range(len(strng)):
        strng[i] = strng[i][::-1]
    return '\n'.join(strng)


def hor_mirror(strng):
    strng = strng.split('\n')
    strngForReturn = []
    for i in range(len(strng)-1, -1, -1):
        strngForReturn.append(strng[i])
    return '\n'.join(strngForReturn)


def oper(fct, s):
    if fct == vert_mirror:
        return vert_mirror(s)
    elif fct == hor_mirror:
        return hor_mirror(s)
    else:
        return False


"""
def vert_mirror(s):
    return "\n".join(line[::-1] for line in s.split("\n"))

def hor_mirror(s):
    return "\n".join(s.split("\n")[::-1])

def oper(fct, s):
    return fct(s)
"""


"""
def vert_mirror(strng):
    return map(reversed, strng)


def hor_mirror(strng):
    return reversed(strng)


def oper(fct, s):
    return '\n'.join(map(''.join, fct(s.split('\n'))))
"""

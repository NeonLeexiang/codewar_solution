def dig_pow(n, p):
    # your code
    nlist = [int(i) for i in str(n)]
    for i in range(len(nlist)):
        nlist[i] **= p
        p += 1
    sumnl = sum(nlist)
    if sumnl % n == 0:
        return sumnl / n
    else:
        return -1


"""
def dig_pow(n, p):
  s = 0
  for i,c in enumerate(str(n)):
     s += pow(int(c),p+i)
  return s/n if s%n==0 else -1
"""

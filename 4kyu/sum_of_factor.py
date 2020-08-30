import math
# from collections import Counter


def factor_list(num):
    lst = []
    tmp = 2
    if num == tmp:
        return [num]
    else:
        while num >= tmp:
            k = num % tmp
            if k == 0:
                lst.append(tmp)
                num = num/tmp
            else:
                tmp = tmp+1
    return list(set(lst))


def factor_list1(n):
    ret = []
    length = int(n/2 + 1)
    for i in range(2, length):
        if n % i == 0:
            k = int(math.sqrt(i) + 1)
            if k == 2:
                ret.append(i)
            else:
                for j in range(2, k):
                        if i % j == 0:
                            break
                        else:
                            ret.append(i)
    return ret


def create_dicts(n):
    n_list = factor_list(abs(n))
    n_dicts = {}
    for c in n_list:
        n_dicts[c] = n
    return n_dicts


def sum_for_list(lst):
    """
    :param lst: list
    :return: list
    """
    # n_dicts
    ret_dicts = {}
    for c in lst:
        """
        ret_dicts = dict(Counter(ret_dicts) + Counter(create_dicts(c)))
        """
        c_dicts = create_dicts(c)
        repeat = [i for i in ret_dicts.keys() if i in c_dicts.keys()]
        for i in repeat:
            c_dicts[i] = ret_dicts[i] + c_dicts[i]
        ret_dicts.update(c_dicts)
    keys, values = ret_dicts.keys(), ret_dicts.values()
    ret_lst = [[keys, values] for keys, values in zip(keys, values)]
    return sorted(ret_lst)


"""
def sum_for_list(lst):
    factors = {i for k in lst for i in xrange(2, abs(k)+1) if not k % i}
    prime_factors = {i for i in factors if not [j for j in factors-{i} if not i % j]}
    return [[p, sum(e for e in lst if not e % p)] for p in sorted(prime_factors)]
"""


"""
from collections import defaultdict
def sum_for_list(lst):

    def factors(x):
        p_facs = []
        i = 2
        while x > 1 or x < -1:
            if x % i == 0:
                p_facs.append(i)
                x //= i
            else:
                i += 1
        return list(set(p_facs))
    
    fac_dict = defaultdict(int)
    
    for i in lst:
        for fac in factors(i):
            fac_dict[fac] += i
            
    return sorted([[k,v] for k,v in fac_dict.items()])
"""


"""
from functools import reduce

def sum_for_list(lst):
    factors = []
    for j in lst: 
        for k in [i for i in range(2, abs(j)+1) if j%i == 0]:
          if factors == [] or reduce(lambda x, y: x and y, [k%m != 0 for m in factors]):
              factors.append(k)
    return [[j, sum([l for l in lst if l%j == 0])] for j in sorted(factors)]
"""

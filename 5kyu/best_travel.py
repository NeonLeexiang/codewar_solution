from itertools import combinations


def choose_best_sum1(t, k, ls):
    ls_com = list(combinations(ls, k))
    ls_com_sum_t = [t - sum(c) for c in ls_com]
    min_l_cst = min([i for i in ls_com_sum_t if i >= 0])
    position = ls_com_sum_t.index(min_l_cst)
    return sum(list(ls_com[position]))


def choose_best_sum(t, k, ls):
    try:
        r = choose_best_sum1(t, k, ls)
        return r
    except(ValueError):
        return None


""""
import itertools
def choose_best_sum(t, k, ls):
    try: 
        return max(sum(i) for i in itertools.combinations(ls,k) if sum(i)<=t)
    except:
        return None
"""


"""
from itertools import combinations

def choose_best_sum(t, k, ls):
    return max((s for s in (sum(dists) for dists in combinations(ls, k)) if s <= t), default=None)
"""

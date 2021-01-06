"""
    date:       2020/9/23 2:28 下午
    written by: neonleexiang
"""
from itertools import combinations
from functools import reduce


# def mul(lst):
#     res = 1
#     for c in lst:
#         res *= c
#     return res


# def product_sum(a, m):
#     """
#
#     :param a: a list of int
#     :param m: int number
#     :return: the product sum
#     """
#     lst = []
#     for c in combinations(a, m):
#         lst.append(reduce(lambda x, y: x * y, c))
#
#     return sum(lst)


"""
    因为我们使用传统循环方法基本上超时了，所以我们在乘积这里使用递归看看能不能
    将时间复杂度降到 O(nlog(n))
    
    GG 递归的方法也没用
"""


# def list_product(lst, size):
#     if size == 0:
#         return 1
#     else:
#         return lst[size-1] * list_product(lst, size - 1)
#
#
# def product_sum(a, m):
#     """
#
#     :param a:
#     :param m:
#     :return:
#     """
#     lst = []
#     for c in combinations(a, m):
#         lst.append(list_product(c, len(c)))
#
#     return sum(lst)


"""
    如果递归的方法都没有效果的话，应该是枚举哪里combinations耗时太长
    要么combinations的时候缩短时间
    要么就是乘积的时候缩短时间
"""


"""
    看完答案之后发现有些人用dp去做，简化了时间复杂度，然后还需要取模
    
"""


def product_sum(xs, m):
    ss = [1] + [0] * m
    for x in xs:
        for i in range(m, 0, -1):
            ss[i] += ss[i - 1] * x
    return ss[m] % (10**9 + 7)

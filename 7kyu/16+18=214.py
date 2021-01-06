"""
    date:       2020/8/30 1:03 下午
    written by: neonleexiang
"""


# def add(num1, num2):
#     res = []
#     lst1 = list(str(num1))
#     lst2 = list(str(num2))
#     for i in range(max(len(lst1), len(lst2))):

"""
def add(a, b):
    s = ""
    while a + b:
        a, p = divmod(a, 10)
        b, q = divmod(b, 10)
        s = str(p + q) + s
    return int(s or '0')
    
    
def add(num1, num2):
    if num1 > num2:
        num2 = str(num2).zfill(len(str(num1)))
        num1 = str(num1)
    else:
        num1 = str(num1).zfill(len((str(num2))))
        num2 = str(num2)
    return int(''.join([str(int(num1[i]) + int(num2[j])) for i in range(len(num1)) for j in range(len(num2)) if i == j]))


"""


if __name__ == '__main__':
    test1 = 166
    test2 = 18
    print(add(16, 18))

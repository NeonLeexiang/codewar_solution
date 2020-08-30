def in_array(array1, array2):
    return_list = []

    for c1 in array1:
        for c2 in array2:
            (s1, s2) = (c1, c2) if (len(c1) < len(c2)) else (c2, c1)
            if s1 in s2:  # and s1 != "46" and s2 != "ode"
                return_list.append(s1)
    return sorted(set(return_list))


""" 
    return_list1 = list(set(return_list))
    return_list1.sort(key = return_list.index)
    return return_list1
"""

"""
def in_array(a1, a2):
    return sorted({sub for sub in a1 if any(sub in s for s in a2)})
"""

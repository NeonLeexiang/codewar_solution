def queue_time(customers, n):
    # TODO
    if customers == [] or n == 0:
        return 0
    elif n > len(customers):
        return max(customers)
    elif n == 1:
        return sum(customers)
    else:
        time = customers[:n]
        for item in customers[n:]:
            a = item + min(time)
            time[time.index(min(time))] = a
        return max(time)


"""
def queue_time(customers, n):
    l=[0]*n
    for i in customers:
        l[l.index(min(l))]+=i
    return max(l)
"""

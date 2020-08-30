def high_and_low(numbers):
    # ...
    num = str.split(numbers, " ")
    numint = [int(item) for item in num]
    numlist = sorted(numint)
    lowest = numlist[0]
    highest = numlist.pop()
    numbers = str(highest) + " " + str(lowest)
    return numbers


"""
def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))
"""

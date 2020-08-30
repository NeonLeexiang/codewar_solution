# math.factorial(n) == n!
import math


def zeros(n):
    n_trailing = str(math.factorial(n))
    for i in range(1, len(n_trailing)):
        if n_trailing[-i] != 0:
            return i


# while version:2.7
# while version:3.4 should pay attention to / and //
"""
def zeros(n):
    count=0
    while n:
        count+=n/5
        n/=5
    return count
"""


# solution from code war
"""
def zeros(n):
  x = n/5
  return x+zeros(x) if x else 0
"""


"""
def zeros(n):
    return 0 if n < 5 else n/5 + zeros(n/5)
"""

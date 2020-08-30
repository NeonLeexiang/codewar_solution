def encode(message, key):
    l1 = len(message) / len(str(key))
    l2 = len(message) % len(str(key))
    key_list = map(int, str(key)*l1+str(key)[:l2])
    mess_list = [ord(c)-96 for c in message]
    return list(map(lambda x: x[0]+x[1], zip(mess_list, key_list)))


"""
from itertools import cycle

def encode(message, key):
    return [ord(a) - 96 + int(b) for a,b in zip(message,cycle(str(key)))]
"""


"""
encode=lambda m,k:[ord(c)-96+int(`k`[i%len(`k`)])for i,c in enumerate(m)]
"""


"""
def encode(message, key):
    return [ ord(char) - 96 + int(str(key)[i % len(str(key))]) for i, char in enumerate(message) ]
"""


"""
def encode(message, key):
    key=str(key)
    return [ord(message[i])-96+int(key[i%len(key)]) for i in range(0, len(message))]
"""


"""
import itertools
import string

def encode(message, key):
    return [string.ascii_lowercase.index(c) + k + 1 for c, k in zip(message, itertools.cycle(int(c) for c in str(key)))]
"""

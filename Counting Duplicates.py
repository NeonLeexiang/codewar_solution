def duplicate_count(text):
    # Your code goes here
    text = str.lower(text)
    count = 0
    for c in text:
        if text.count(c)>1:
            text = text.replace(c, '')
            count = count + 1
    return count


"""
def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])
     
"""


"""
from collections import Counter

def duplicate_count(text):
    return sum(1 for c, n in Counter(text.lower()).iteritems() if n > 1)
     
"""

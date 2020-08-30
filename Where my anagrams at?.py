def anagrams(word, words):
    #your code here
    wordsort = [''.join(sorted(word))]
    w2 = [sorted(item) for item in words]
    w2 = [''.join(item) for item in w2]
    rword = []
    count = 0
    for item in w2:
        if item == wordsort[0]:
            rword.append(words[count])
            count += 1
        else:
            rword.extend([])
            count += 1
    return rword


"""
def anagrams(word, words): 
    return [item for item in words if sorted(item)==sorted(word)]
"""


"""
def anagrams(word, words):
    return filter(lambda x: sorted(word) == sorted(x), words)
"""

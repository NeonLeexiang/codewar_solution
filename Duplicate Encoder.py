def duplicate_encode(word):
    #your code here
    wordlist = list(word)
    wordprint=""
    for i in range(len(word)):
        word1=wordlist[:i]+wordlist[i+1:]
        if wordlist[i] in word1:
            wordprint=wordprint+")"
        else:
            wordprint=wordprint+"("
    return wordprint


"""
    def duplicate_encode(word):
        return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])
"""


"""
    from collections import Counter

    
    def duplicate_encode(word):
        word = word.lower()
        counter = Counter(word)
        return ''.join(('(' if counter[c] == 1 else ')') for c in word)
"""

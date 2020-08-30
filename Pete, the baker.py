def cakes(recipe, available):
    from collections import Counter
    alen = len(available)
    a = available
    count = -1
    if set(recipe).issubset(set(available)):
        while(len(available) - alen == 0):
            a = available
            available = dict(Counter(available) - Counter(recipe))
            count += 1
        for key in recipe:
            if recipe[key] == a[key]:
                return count + 1
        return count
    else:
        return count + 1



"""
def cakes(recipe, available):
  return min(available.get(k, 0)/recipe[k] for k in recipe)
"""


"""
def cakes(recipe, available):
    return min(available.get(k, 0) // v for k,v in recipe.iteritems())
"""


"""
def cakes(recipe, available):
    try:
        return min([available[a]/recipe[a] for a in recipe])
    except:
        return 0
"""

""""
def remove_rotten(bag_of_fruits):
    return [x.replace('rotten', '').lower() for x in bag_of_fruits] if bag_of_fruits else []
"""


def remove_rotten(bag_of_fruits):
    if bag_of_fruits == None:
        return []
    for i in range(len(bag_of_fruits)):
        bag_of_fruits[i] = str.lower(bag_of_fruits[i][6:]) if bag_of_fruits[:6] == "rotten"
        # else bag_of_fruits[i] = bag_of_fruits[i]
    return bag_of_fruits

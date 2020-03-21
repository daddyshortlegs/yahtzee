def ones(rolls):
    return sum(filter(lambda roll: roll == 1, rolls))

def twos(rolls):
    return sum(filter(lambda roll: roll == 2, rolls))

def threes(rolls):
    return sum(filter(lambda roll: roll == 3, rolls))
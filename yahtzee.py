def ones(rolls):
    return sum(filter(lambda roll: roll == 1, rolls))

def twos(rolls):
    return sum(filter(lambda roll: roll == 2, rolls))

def threes(rolls):
    return sum(filter(lambda roll: roll == 3, rolls))

def fours(rolls):
    return sum(filter(lambda roll: roll == 4, rolls))

def fives(rolls):
    return sum(filter(lambda roll: roll == 5, rolls))

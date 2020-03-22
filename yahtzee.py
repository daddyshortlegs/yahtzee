def ones(rolls):
    return score_singles(rolls, 1)

def twos(rolls):
    return score_singles(rolls, 2)

def threes(rolls):
    return score_singles(rolls, 3)

def fours(rolls):
    return score_singles(rolls, 4)

def fives(rolls):
    return score_singles(rolls, 5)

def sixes(rolls):
    return score_singles(rolls, 6)

def score_singles(rolls, value):
    return sum(filter(lambda roll: roll == value, rolls))

def count_dice(dice):
    result = [0, 0, 0, 0, 0, 0]
    for die in dice:
        result[die - 1] += 1

    return result





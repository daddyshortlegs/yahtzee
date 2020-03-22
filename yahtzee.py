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

def pair(dice):
    return x_of_a_kind(dice, 2)

def three_of_a_kind(dice):
    return x_of_a_kind(dice, 3)

def four_of_a_kind(dice):
    return x_of_a_kind(dice, 4)

def x_of_a_kind(dice, value_count):
    counts = count_dice(dice)
    if value_count in counts:
        return (counts.index(value_count) + 1) * value_count
    return 0

def yahtzee(dice):
    if 5 in count_dice(dice):
        return 50

    return 0




def count_dice(dice):
    result = [0, 0, 0, 0, 0, 0]
    for die in dice:
        result[die - 1] += 1

    return result





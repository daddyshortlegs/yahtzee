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

def small_straight(dice):
    return calc_straight([1, 1, 1, 1, 1, 0], dice)

def large_straight(dice):
    return calc_straight([0, 1, 1, 1, 1, 1], dice)

def calc_straight(counts, dice):
    if count_dice(dice) == counts:
        return sum(dice)
    return 0

def full_house(dice):
    two = pair(dice)
    three = three_of_a_kind(dice)
    if two != 0 and three != 0:
        return two + three

    return 0


def yahtzee(dice):
    if 5 in count_dice(dice):
        return 50

    return 0

def chance(dice):
    return sum(dice)



def count_dice(dice):
    result = [0, 0, 0, 0, 0, 0]
    for die in dice:
        result[die - 1] += 1

    return result




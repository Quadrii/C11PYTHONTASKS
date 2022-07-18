import random

one_tally = 0
two_tally = 0
three_tally = 0
four_tally = 0
five_tally = 0
six_tally = 0


def roll():
    die = random.randint(1, 7)
    return die


for rolling in range(10_000):
    if roll() == 1:
        one_tally = one_tally + 1
    elif roll() == 2:
        two_tally = two_tally + 1
    elif roll() == 3:
        three_tally = three_tally + 1
    elif roll() == 4:
        four_tally = four_tally + 1
    elif roll() == 5:
        five_tally = five_tally + 1
    elif roll() == 6:
        six_tally = six_tally + 1
print()
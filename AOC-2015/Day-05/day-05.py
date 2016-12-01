import re
from itertools import groupby

__author__ = 'Géraud'


def puzzle_1(string):
    if any(char in string for char in ["ab", "cd", "pq", "xy"]):
        return 0
    elif sum((1 if char in "aeiou" else 0 for char in string)) < 3:
        return 0
    elif sum([1 if len(list(group)) > 1 else 0 for key, group in groupby(string)]) < 1:
        return 0
    else:
        return 1


def puzzle_2(string):
    # letter repeat
    if not re.search(r'(.).(\1)', string):
        return 0

    # pair repeat
    if not re.search(r'(..).*(\1)', string):
        return 0

    return 1


if __name__ == '__main__':
    good_strings_1 = 0
    good_strings_2 = 0

    with open('input.txt', 'r') as file:
        for string in file.read().splitlines():
            good_strings_1 += puzzle_1(string)
            good_strings_2 += puzzle_2(string)

    print("Puzzle 1: %d" % good_strings_1)
    print("Puzzle 2: %d" % good_strings_2)

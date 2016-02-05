from operator import add
from functools import reduce

__author__ = 'Géraud'

if __name__ == "__main__":
    input = 34000000
    score_part_1 = 0
    score_part_2 = 0
    part_1 = None
    part_2 = None

    print("Computing (can take about a minute)")
    for house in range(100000, 34000000):
        divisors = set(reduce(add, ([i, house//i] for i in range(1, int(house**0.5) + 1) if house % i == 0)))
        if not part_1:
            score_part_1 = sum(divisors) * 10
            if score_part_1 >= input:
                print("Part 1: {}".format(house))
                if part_2:
                    exit()
                part_1 = True
        if not part_2:
            score_part_2 = sum(filter(lambda x: house / x < 50, divisors)) * 11
            if score_part_2 >= input:
                print("Part 2: {}".format(house))
                if part_1:
                    exit()
                part_2 = True

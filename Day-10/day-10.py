from itertools import groupby


__author__ = 'Géraud'

if __name__ == '__main__':
    num = "3113322113"
    for _ in range(40):
        num = ''.join([str(len(tuple(group))) + key for key, group in groupby(num)])
    print("Part 1: %d" % len(num))

    # We already calculated until 40, so we keep the result and iter 10 more times
    for _ in range(10):
        num = ''.join([str(len(tuple(group))) + key for key, group in groupby(num)])
    print("puzzle 2: %d" % len(num))

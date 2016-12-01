import hashlib
import itertools


__author__ = 'Géraud'


def resolve_puzzle(str_input, start, end_condition):
    for n in itertools.count(start):
        if hashlib.md5((str_input + str(n)).encode()).hexdigest().startswith(end_condition):
            return n


def puzzle_2():
    pass


if __name__ == '__main__':
    puzzle_input = "bgvyzdsv"

    soluce_1 = resolve_puzzle(puzzle_input, 0, '00000')
    print("Puzzle 1: %d" % soluce_1)

    soluce_2 = resolve_puzzle(puzzle_input, soluce_1, '000000')
    print("Puzzle 2: %d" % soluce_2)

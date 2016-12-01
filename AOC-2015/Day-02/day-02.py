from functools import reduce
import operator

__author__ = 'Géraud'


def puzzle_1(l, w, h):
    sides = [l * w, w * h, h * l]
    return sum(2 * side for side in sides) + min(sides)


def puzzle_2(instructions):
    bow = reduce(operator.mul, instructions, 1)
    instructions.sort()
    return sum(2 * side for side in instructions[:-1]) + bow


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        instructions = [list(map(int, line.split('x'))) for line in file]
        wrapping_paper_surface = 0
        ribbon_length = 0

        for instruction in instructions:
            wrapping_paper_surface += puzzle_1(*instruction)
            ribbon_length += puzzle_2(instruction)

        print("Puzzle 1: %d" % wrapping_paper_surface)
        print("Puzzle 2: %d" % ribbon_length)

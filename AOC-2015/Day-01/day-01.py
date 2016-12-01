__author__ = 'Géraud'


def puzzle_1(instructions):
    result = sum([-1 if instruction == ")" else 1 for instruction in instructions])
    return result


def puzzle_2(instructions):
    position = 0
    floor = 0
    for instruction in instructions:
        floor = floor - 1 if instruction == ")" else floor + 1
        position += 1
        if floor == -1:
            return position


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        instructions = file.read()
        print("Puzzle 1: %d" % puzzle_1(instructions))
        print("Puzzle 2: %d" % puzzle_2(instructions))

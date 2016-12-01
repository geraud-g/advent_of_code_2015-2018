__author__ = 'Géraud'


def puzzle_1(instructions, directions):
    coord = (0, 0)
    houses_visited = {str(coord)}

    for instruction in instructions:
        coord = directions[instruction](*coord)
        houses_visited.add(str(coord))

    return len(houses_visited)


def puzzle_2(instructions, directions):
    coord_santa = (0, 0)
    coord_robot = (0, 0)
    turn = 0

    houses_visited = {str(coord_santa)}

    for instruction in instructions:
        if turn % 2 == 0:
            coord_santa = directions[instruction](*coord_santa)
            houses_visited.add(str(coord_santa))
        else:
            coord_robot = directions[instruction](*coord_robot)
            houses_visited.add(str(coord_robot))
        turn += 1
    return len(houses_visited)


if __name__ == '__main__':

    directions = {
        'v': lambda x, y: (x, y + 1),
        '^': lambda x, y: (x, y - 1),
        '<': lambda x, y: (x - 1, y),
        '>': lambda x, y: (x + 1, y)
    }

    with open('input.txt', 'r') as file:
        instructions = file.read()
        houses_puzzle_1 = puzzle_1(instructions, directions)
        houses_puzzle_2 = puzzle_2(instructions, directions)

        print("Puzzle 1: %d" % houses_puzzle_1)
        print("Puzzle 2: %d" % houses_puzzle_2)

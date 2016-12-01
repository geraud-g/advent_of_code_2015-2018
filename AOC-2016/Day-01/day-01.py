import re

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


def manhattan_distance(coord):
    return abs(coord[0] + coord[1])


def travel(instructions):
    """ Return a list containing each coordinate visited
    """
    turns = {'L': -1, 'R': 1}
    direction = NORTH
    path = [(0, 0)]
    actions = {
        NORTH: lambda dist, y, x: [(y + i, x) for i in range(1, dist + 1)],
        EAST: lambda dist, y, x: [(y, x + i) for i in range(1, dist + 1)],
        SOUTH: lambda dist, y, x: [(y - i, x) for i in range(1, dist + 1)],
        WEST: lambda dist, y, x: [(y, x - i) for i in range(1, dist + 1)],
    }

    for turn, distance in instructions:
        current_position = path[-1]
        distance = int(distance)
        direction = (direction + turns[turn]) % 4
        new_path = actions[direction](distance, *current_position)
        path += new_path
    return path


if __name__ == "__main__":
    with open('input.txt') as f:
        file = f.read()
        instructions = re.findall(r'([LR])([0-9]+)', file)
        path = travel(instructions)

        # Puzzle 1: get the manhattan distance between 0,0 and the last location visited
        distance_from_HQ = manhattan_distance(path[-1])
        print("Puzzle 1: {}".format(distance_from_HQ))

        # Puzzle 2: get the manhattan distance between 0,0 and the first location visited twice
        visited_twice = [coord for index, coord in enumerate(path) if coord in path[:index]]
        distance_from_first_visited_twice = manhattan_distance(visited_twice[0])
        print("Puzzle 2: {}".format(distance_from_first_visited_twice))

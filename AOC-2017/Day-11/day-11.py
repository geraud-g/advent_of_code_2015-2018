def get_input() -> [str]:
    with open('input.txt') as f:
        line = f.readline().strip()
        return line.split(',')


def get_distance(y: int, x: int, z: int) -> int:
    return (abs(x) + abs(y) + abs(z)) // 2


def solve_puzzle(path: [str]) -> (int, int):
    y = x = z = 0
    max_distance = 0

    directions = {
        'n': (-1, 0, 1),
        's': (1, 0, -1),
        'ne': (-1, 1, 0),
        'nw': (0, -1, 1),
        'se': (0, 1, -1),
        'sw': (1, -1, 0)
    }
    for direction in path:
        tmp_y, tmp_x, tmp_z = directions[direction]
        y += tmp_y
        x += tmp_x
        z += tmp_z
        max_distance = max(max_distance, get_distance(y, x, z))
    distance = get_distance(y, x, z)
    return distance, max_distance


if __name__ == "__main__":
    puzzle_input = get_input()
    solution_1, solution_2 = solve_puzzle(puzzle_input)

    print(f'Part 1: {solution_1}')
    print(f'Part 2: {solution_2}')

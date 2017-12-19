UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
EMPTY = ' '


def get_input() -> [str]:
    with open('input.txt') as f:
        return [line.strip('\n') for line in f.readlines()]


def find_start_coord(maze) -> (int, int):
    for index, value in enumerate(maze[0]):
        if value == '|':
            return 0, index


def get_new_direction(maze: [str], y: int, x: int, direction: str) -> str:
    try:
        left = maze[y][x - 1]
    except IndexError:
        left = ' '
    try:
        up = maze[y - 1][x]
    except IndexError:
        up = ' '
    if direction in (DOWN, UP):
        return LEFT if left != EMPTY else RIGHT
    else:
        return UP if up != EMPTY else DOWN


def get_next_tile(maze: [str], y: int, x: int, direction: str) -> (int, int, str):
    if maze[y][x] == '+':
        direction = get_new_direction(maze, y, x, direction)
    return {
        UP: (y - 1, x, direction),
        DOWN: (y + 1, x, direction),
        LEFT: (y, x - 1, direction),
        RIGHT: (y, x + 1, direction)
    }[direction]


def solve_puzzle(maze: [str]) -> (str, int):
    y, x = find_start_coord(maze)
    letters_encountered = []
    current_tile = None
    direction = DOWN
    counter = 0

    while current_tile != EMPTY:
        try:
            current_tile = maze[y][x]
            if current_tile.isalpha():
                letters_encountered.append(current_tile)
            y, x, direction = get_next_tile(maze, y, x, direction)
            counter += 1
        except IndexError:
            break
    return ''.join(letters_encountered), counter


if __name__ == "__main__":
    puzzle_input = get_input()
    letters, steps = solve_puzzle(puzzle_input)
    print(f'Part 1: {letters}')
    print(f'Part 2: {steps}')

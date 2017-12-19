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


def get_cross_next_tile(maze, y, x, direction):
    try:
        left = maze[y][x - 1]
    except IndexError:
        left = ' '
    try:
        up = maze[y - 1][x]
    except IndexError:
        up = ' '
    if direction in (DOWN, UP):
        if left != ' ':
            return y, x - 1, LEFT
        else:
            return y, x + 1, RIGHT
    else:
        if up != ' ':
            return y -1, x, UP
        else:
            return y + 1, x, DOWN


def get_next_tile(maze, y, x, direction):
    current_tile = maze[y][x]

    if current_tile in ['|', '-']:
        if direction == DOWN:
            return y + 1, x, direction
        elif direction == UP:
            return y - 1, x, direction
        if direction == RIGHT:
            return y, x + 1, direction
        else:
            return y, x - 1, direction
    elif current_tile == '+':
        return get_cross_next_tile(maze, y, x, direction)
    else:
        if direction == UP:
            return y-1, x, direction
        elif direction == DOWN:
            return y+1, x, direction
        elif direction == RIGHT:
            return y, x+1, direction
        else:
            return y, x-1, direction


def solve_puzzle(maze: [str]):
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
            new_y, new_x, new_direction = get_next_tile(maze, y, x, direction)
            y, x, direction = new_y, new_x, new_direction
            counter += 1
        except IndexError:
            break
    print(''.join(letters_encountered) == 'KGPTMEJVS')
    print(counter == 16328)


if __name__ == "__main__":
    puzzle_input = get_input()
    solution_1 = solve_puzzle(puzzle_input)
    print(f'Part 1: {solution_1}')

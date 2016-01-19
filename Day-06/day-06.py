import re

__author__ = 'Géraud'


def turn(grid, corners, set_to):
    x_start, y_start, x_end, y_end = corners
    for y in range(y_start, y_end + 1):
        for x in range(x_start, x_end + 1):
            grid[y][x] = set_to


def toggle(grid, corners):
    x_start, y_start, x_end, y_end = corners
    for y in range(y_start, y_end + 1):
        for x in range(x_start, x_end + 1):
            grid[y][x] = (grid[y][x] + 1) % 2


def puzzle_1(grid, instruction):
    regex = r'^[a-zAZ ]+(\d+),(\d+)[a-zAZ ]+(\d+),(\d+)$'
    corners = [int(n) for n in re.findall(regex, instruction)[0]]

    if instruction.startswith("turn on"):
        turn(grid, corners, 1)
    elif instruction.startswith("turn off"):
        turn(grid, corners, 0)
    elif instruction.startswith("toggle"):
        toggle(grid, corners)


def puzzle_2(grid, instruction):
    regex = r'^[a-zAZ ]+(\d+),(\d+)[a-zAZ ]+(\d+),(\d+)$'
    x_start, y_start, x_end, y_end = [int(n) for n in re.findall(regex, instruction)[0]]
    values = {
        "turn on": 1,
        "turn of": -1,
        "toggle ": 2
    }
    for y in range(y_start, y_end + 1):
        for x in range(x_start, x_end + 1):
            grid[y][x] += values[instruction[:7]]
            grid[y][x] = 0 if grid[y][x] < 0 else grid[y][x]


if __name__ == '__main__':
    grid_1 = [[0 for x in range(1000)] for x in range(1000)]
    grid_2 = [grid[:] for grid in grid_1]

    with open('input.txt', 'r') as file:
        for instruction in file.read().splitlines():
            puzzle_1(grid_1, instruction)
            puzzle_2(grid_2, instruction)

    print("Puzzle 1: %d" % sum(map(sum, grid_1)))
    print("Puzzle 2: %d" % sum(map(sum, grid_2)))


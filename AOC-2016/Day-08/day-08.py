import re


GRID_HEIGHT = 6
GRID_WIDTH = 50
FULL_CELL = '█'
EMPTY_CELL = ' '


def process(instruction, grid):
    found = re.search(r'rect (\d+)x(\d+)', instruction)
    if found:
        rx = int(found.group(1))
        ry = int(found.group(2))

        for y in range(ry):
            for x in range(rx):
                grid[y] = list(grid[y])
                grid[y][x] = FULL_CELL
        return grid

    found = re.search(r'rotate row y=(\d+) by (\d+)', instruction)
    if found:
        y = int(found.group(1)) % GRID_HEIGHT
        val = int(found.group(2)) % GRID_WIDTH
        grid[y] = grid[y][-val:] + grid[y][:-val]
        return grid

    found = re.search(r'rotate column x=(\d+) by (\d+)', instruction)
    if found:
        grid = list(zip(*grid))
        y = int(found.group(1)) % GRID_WIDTH
        val = int(found.group(2)) % GRID_HEIGHT
        grid[y] = grid[y][-val:] + grid[y][:-val]
        grid = list(zip(*grid))
        return grid


if __name__ == "__main__":
    grid = []
    for _ in range(GRID_HEIGHT):
        grid.append([EMPTY_CELL] * GRID_WIDTH)

    with open("input.txt") as f:
        file = f.readlines()

    for instruction in file:
        grid = process(instruction, grid)

    count = 0
    for line in grid:
        count += sum(c == FULL_CELL for c in line)

    print("Puzzle 1: {}".format(count))

    print("Puzzle 2:")
    for line in grid:
        line = ''.join(line)
        print(' '.join([line[x:x + 5] for x in range(0, GRID_WIDTH, 5)]))

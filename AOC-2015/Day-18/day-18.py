
__author__ = 'Géraud'


def init_grid():
    with open("input.txt") as file:
        file = file.readlines()
    new_grid = []
    for line in file:
        new_grid.append([True if instruction == "#" else False for instruction in line[:-1]])
    return new_grid


def get_neighbors_on(grid, y, x):
    min_x = x - 1 if x > 0 else 0
    r1 = grid[y - 1][min_x:x + 2] if y > 0 else []
    r2 = grid[y][min_x:x + 2]
    r3 = grid[y + 1][min_x:x + 2] if y + 1 < len(grid) else []
    count = sum(r1 + r2 + r3)
    return count if not grid[y][x] else (count - 1)


def update_light(grid, new_grid, y, x):
    nbr_neighbors_on = get_neighbors_on(grid, y, x)
    if grid[y][x] == True and not (nbr_neighbors_on == 2 or nbr_neighbors_on == 3):
        new_grid[y][x] = False
    elif grid[y][x] == False and nbr_neighbors_on == 3:
        new_grid[y][x] = True


def light_corners(grid):
    end_y = len(grid) - 1
    end_x = len(grid[0]) - 1
    corners = ((0, 0), (0, end_x), (end_y, 0), (end_y, end_x))
    for x, y in corners:
        grid[y][x] = True


def process(puzzle=1):
    grid = init_grid()
    if puzzle == 2:
        light_corners(grid)
    steps = 100
    for step in range(steps):
        new_grid = [row.copy() for row in grid]
        for y1, row in enumerate(grid):
            for x1, tile in enumerate(row):
                update_light(grid, new_grid, y1, x1)
        grid = new_grid
        if puzzle == 2:
            light_corners(grid)

    nbr_on = sum([sum(x) for x in grid])
    print("Part {}: {}".format(puzzle, nbr_on))

if __name__ == "__main__":
    process(puzzle=1)
    process(puzzle=2)

from collections import defaultdict


SPACE = '.'
WALL = '#'
FAVORITE_NBR = 1358  # 10
START = (1, 1)
GOAL = (39, 31)


def space_or_wall(maze, coord):
    y, x = coord
    if x in maze[y]:
        return coord[y][x]
    result = x * x + 3 * x + 2 * x * y + y + y * y + FAVORITE_NBR
    ones_in_result = sum(c == '1' for c in bin(result)[2:])
    return WALL if ones_in_result % 2 else SPACE


def get_neighbours(coord, maze, path):
    y, x = coord
    neighbours = [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]
    valid_neighbours = []

    for neighbour in neighbours:
        tmp_y, tmp_x = neighbour

        if neighbour in path or tmp_y < 0 or tmp_x < 0:
            continue
        if space_or_wall(maze, neighbour) == SPACE:
            valid_neighbours.append(neighbour)
    return valid_neighbours


def bfs(maze, start, goal):
    queue = [(start, [start])]

    while queue:
        (coord, path) = queue.pop(0)
        for next_coord in get_neighbours(coord, maze, path):
            if next_coord == goal:
                return path + [next_coord]
            else:
                queue.append((next_coord, path + [next_coord]))
    return None


def bfs_part_2(maze, start):
    queue = [(start, [start])]
    visited = set([start])

    while queue:
        (coord, path) = queue.pop(0)
        for next_coord in get_neighbours(coord, maze, path):
            visited.add(next_coord)
            if len(path) < 50:
                queue.append((next_coord, path + [next_coord]))
    return visited


if __name__ == "__main__":
    maze = defaultdict(dict)
    path = bfs(maze, START, GOAL)
    print("Puzzle 1: {} steps".format(len(path) - 1))

    visited = bfs_part_2(maze, START)
    print("Puzzle 2: {} locations visited".format(len(visited)))

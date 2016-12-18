from hashlib import md5

PASSCODE = 'yjjvjgan'


def get_open_doors(coord, directions):
    y, x = coord
    open_doors = []
    path = PASSCODE + directions
    hash_value = md5(path.encode()).hexdigest()
    moves = [("U", (y - 1, x)),
             ("D", (y + 1, x)),
             ("L", (y, x - 1)),
             ("R", (y, x + 1))]

    for index, move in enumerate(moves):
        direction, coord = move
        tmp_y, tmp_x = coord

        if not (0 <= tmp_y < 4 and 0 <= tmp_x < 4):
            continue
        if hash_value[index] in 'bcdef':
            open_doors.append(move)

    return open_doors


def bfs(start, goal):
    directions = ""
    queue = [(start, [start], directions)]
    paths = []

    while queue:
        (coord, path, directions) = queue.pop(0)
        for next_direction, next_coord in get_open_doors(coord, directions):
            if next_coord == goal:
                paths.append(directions + next_direction)
            else:
                queue.append((next_coord, path + [next_coord], directions + next_direction))
    return paths


if __name__ == "__main__":
    paths = bfs((0, 0), (3, 3))
    shorted_path = paths[0]
    max_len_path = len(max(paths, key=len))

    print("Puzzle 1: {}".format(shorted_path))
    print("Puzzle 2: {}".format(max_len_path))

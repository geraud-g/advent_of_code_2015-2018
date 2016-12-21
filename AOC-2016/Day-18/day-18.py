SAFE = True
TRAP = False


def puzzle(rows_nbr):
    prev_row = '.^.^..^......^^^^^...^^^...^...^....^^.^...^.^^^^....^...^^.^^^...^^^^.^^.^.^^..^.^^^..^^^^^^.^^^..^'
    prev_row = [c == '.' for c in prev_row]
    row_len = len(prev_row)
    count = sum(prev_row)

    for y in range(1, rows_nbr):
        new_row = []
        prev_row = [SAFE] + prev_row + [SAFE]

        for x in range(1, row_len + 1):
            new_row.append(prev_row[x - 1] == prev_row[x + 1])
        count += sum(new_row)
        prev_row = new_row
    return count


if __name__ == "__main__":
    safe_rows = puzzle(40)
    print("Puzzle 1: {}".format(safe_rows))

    safe_rows = puzzle(400000)
    print("Puzzle 2: {}".format(safe_rows))

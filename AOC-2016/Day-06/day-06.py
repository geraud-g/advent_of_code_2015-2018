import collections


if __name__ == "__main__":
    puzzle_1 = ""
    puzzle_2 = ""

    with open("input.txt") as f:
        file = f.read()
    file = file.split()
    colomns = zip(*file)

    for col in colomns:
        count = collections.Counter(col)
        most_used = max(count, key=lambda x: count[x])
        less_used = min(count, key=lambda x: count[x])
        puzzle_1 += most_used
        puzzle_2 += less_used

    print("Puzzle 1: {}".format(puzzle_1))
    print("Puzzle 2: {}".format(puzzle_2))

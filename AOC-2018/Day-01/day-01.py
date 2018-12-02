import itertools


def read_file() -> [int]:
    with open("input.txt") as f:
        return [int(line) for line in f.readlines()]


def puzzle_part_b() -> int:
    changes = read_file()
    computed_frequencies = {0}
    frequency = 0

    for change in itertools.cycle(changes):
        frequency += change
        if frequency in computed_frequencies:
            break
        computed_frequencies.add(frequency)
    return frequency


def puzzle_part_a() -> int:
    changes = read_file()
    return sum(changes)


if __name__ == "__main__":
    result_a = puzzle_part_a()
    print(f"Puzzle part 1: {result_a}")
    result_b = puzzle_part_b()
    print(f"Puzzle part 2: {result_b}")

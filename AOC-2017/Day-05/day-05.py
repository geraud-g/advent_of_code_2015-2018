def get_input() -> [int]:
    with open('input.txt') as f:
        return [int(x) for x in f.readlines()]


def puzzle_part_1(jumps: [int], part: int=1) -> int:
    offset = 0
    steps = 0

    while True:
        try:
            last_offset = offset
            offset = offset + jumps[offset]
            steps += 1

            if part == 1:
                jumps[last_offset] += 1
        except IndexError:
            return steps


if __name__ == "__main__":
    jumps = get_input()

    result_1 = puzzle_part_1(jumps, part=1)
    print(f"Puzzle 1: {result_1}")

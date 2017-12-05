def get_input() -> [int]:
    with open('input.txt') as f:
        return [int(x) for x in f.readlines()]


def make_jumps(jumps: [int], part: int=1) -> int:
    offset = 0
    steps = 0

    while True:
        try:
            last_offset = offset
            offset = offset + jumps[offset]
            steps += 1

            if part == 1 or jumps[last_offset] < 3:
                jumps[last_offset] += 1
            else:
                jumps[last_offset] -= 1
        except IndexError:
            return steps


if __name__ == "__main__":
    jumps = get_input()
    result_1 = make_jumps(jumps, part=1)
    print(f"Puzzle 1: {result_1}")

    jumps = get_input()
    result_2 = make_jumps(jumps, part=2)
    print(f"Puzzle 2: {result_2}")

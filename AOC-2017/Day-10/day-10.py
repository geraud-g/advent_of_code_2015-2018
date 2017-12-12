def get_input() -> [str]:
    with open('input.txt') as f:
        line = f.readline()
        return [int(x) for x in line.split(', ')]


def solve_puzzle(lengths):
    print(lengths)
    return 1


if __name__ == "__main__":
    puzzle_input = get_input()
    solution_1 = solve_puzzle(puzzle_input)
    # print(f'Part 1: {solution_1}')
    # print(f'Part 2: {solution_2}')

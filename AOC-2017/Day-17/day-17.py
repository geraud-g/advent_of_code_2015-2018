from collections import deque


def get_input() -> int:
    with open('input.txt') as f:
        return int(f.readline().strip())


def solve_puzzle(steps_nbr: int, part: int=1) -> int:
    state = deque([0])

    iterations = 2017 if part == 1 else 50000000

    for value in range(1, iterations + 1):
        state.rotate(-steps_nbr)
        state.append(value)

    if part == 1:
        solution = state[0]
    else:
        solution = state[(state.index(0) + 1) % len(state)]
    return solution


if __name__ == "__main__":
    puzzle_input = get_input()

    solution_1 = solve_puzzle(puzzle_input, part=1)
    print(f'Part 1: {solution_1}')

    solution_2 = solve_puzzle(puzzle_input, part=2)
    print(f'Part 2: {solution_2}')

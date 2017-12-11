import re


def get_input() -> str:
    with open('input.txt') as f:
        line = f.readline()
    return re.sub(r'!.', '', line)


def solve_puzzle(stream: str) -> (int, int):
    score = 0
    depth = 0
    garbage_total_len = 0
    garbage = False

    for char in stream:
        if garbage and char != '>':
            garbage_total_len += 1
        elif char == '<':
            garbage = True
        elif char == '>':
            garbage = False
        elif char == '{':
            score += (depth + 1)
            depth += 1
        elif char == '}':
            depth -= 1

    return score, garbage_total_len


if __name__ == "__main__":
    puzzle_input = get_input()
    solution_1, solution_2 = solve_puzzle(puzzle_input)
    print(f'Part 1: {solution_1}')
    print(f'Part 2: {solution_2}')

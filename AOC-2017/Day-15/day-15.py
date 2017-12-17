import re

from typing import Generator

FACTOR_A = 16807
FACTOR_B = 48271
MODULO = 2147483647


def get_input() -> (int, int):
    with open('input.txt') as f:
        line = f.readline()
        search_a = re.search(r'Generator A starts with (\w+)', line)
        input_a = int(search_a.group(1))

        line = f.readline()
        search_b = re.search(r'Generator B starts with (\w+)', line)
        input_b = int(search_b.group(1))
    return input_a, input_b


def solve_puzzle(a_value: int, b_value: int) -> int:
    counter = 0
    mask = 0xFFFF

    for _ in range(40000000):
        a_value = (a_value * FACTOR_A) % MODULO
        b_value = (b_value * FACTOR_B) % MODULO
        if a_value & mask == b_value & mask:
            counter += 1
    return counter


def value_generator(start_value: int, factor: int, multiple_of: int) -> Generator[int]:
    while True:
        start_value = (start_value * factor) % MODULO
        if start_value % multiple_of == 0:
            yield start_value


def solve_puzzle_2(a_start_value: int, b_start_value: int) -> int:
    mask = 0xFFFF
    counter = 0
    a_value_generator = value_generator(a_start_value, FACTOR_A, 4)
    b_value_generator = value_generator(b_start_value, FACTOR_B, 8)

    for _ in range(5000000):
        a_value = next(a_value_generator)
        b_value = next(b_value_generator)
        if a_value & mask == b_value & mask:
            counter += 1

    return counter


if __name__ == "__main__":
    a, b = get_input()

    solution_1 = solve_puzzle(a, b)
    print(f'Part 1: {solution_1}')

    solution_2 = solve_puzzle_2(a, b)
    print(f'Part 2: {solution_2}')

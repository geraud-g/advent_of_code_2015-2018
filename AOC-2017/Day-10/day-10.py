from functools import reduce
from operator import xor


def get_input(part: int=1) -> [str]:
    with open('input.txt') as f:
        line = f.readline().strip()
    if part == 1:
        return [int(x) for x in line.split(',')]
    else:
        return list(map(ord, line)) + [17, 31, 73, 47, 23]


def reverse_sub_list(circular_list: [int], current_position: int, length: int) -> [int]:
    list_len = len(circular_list)

    for x in range(length // 2):
        start = (current_position + x) % list_len
        end = (current_position - x + length - 1) % list_len
        circular_list[start], circular_list[end] = circular_list[end], circular_list[start]
    return circular_list


def solve_part_1(lengths: [int]) -> int:
    circular_list = list(range(256))
    current_position = 0
    skip_size = 0

    for length in lengths:
        reverse_sub_list(circular_list, current_position, length)
        current_position += (length + skip_size)
        skip_size += 1
    return circular_list[0] * circular_list[1]


def knot_hash(lengths: [int]) -> str:
    circular_list = list(range(256))
    current_position = 0
    skip_size = 0

    for _ in range(64):
        for length in lengths:
            reverse_sub_list(circular_list, current_position, length)
            current_position += (length + skip_size)
            skip_size += 1

    dense_hash = []
    for x in range(0, 256, 16):
        dense_hash += [reduce(xor, circular_list[x:x+16])]
    formatted_hash = ''.join(f'{x:0{2}x}' for x in dense_hash)
    return formatted_hash


if __name__ == "__main__":
    puzzle_input = get_input(part=1)

    solution_1 = solve_part_1(puzzle_input)
    print(f'Part 1: {solution_1}')
    puzzle_input = get_input(part=2)

    solution_2 = knot_hash(puzzle_input)
    print(f'Part 2: {solution_2}')


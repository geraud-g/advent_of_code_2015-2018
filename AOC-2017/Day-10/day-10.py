def get_input() -> [str]:
    with open('input.txt') as f:
        line = f.readline()
        return [int(x) for x in line.split(',')]


def reverse_sub_list(circular_list, current_position, length):
    list_len = len(circular_list)

    for x in range(length // 2):
        start = (current_position + x) % list_len
        end = (current_position - x + length - 1) % list_len
        circular_list[start], circular_list[end] = circular_list[end], circular_list[start]
    return circular_list


def solve_puzzle(lengths: [int]) -> int:
    circular_list = list(range(256))
    current_position = 0
    skip_size = 0

    for length in lengths:
        reverse_sub_list(circular_list, current_position, length)
        current_position += (length + skip_size)
        skip_size += 1
    return circular_list[0] * circular_list[1]


if __name__ == "__main__":
    puzzle_input = get_input()

    solution_1 = solve_puzzle(puzzle_input)
    print(f'Part 1: {solution_1}')

def get_input() -> [int]:
    dict_firewall = {}

    with open('input.txt') as f:
        lines = f.readlines()

    for line in lines:
        layer_depth, layer_range = map(int, line.split(': '))
        dict_firewall[layer_depth] = layer_range
    max_depth = max(dict_firewall)
    list_firewall = [0] * (max_depth + 1)
    for layer_depth, layer_range in dict_firewall.items():
        list_firewall[layer_depth] = layer_range
    return list_firewall


def has_been_caught(turn: int, scanner_range: int) -> bool:
    if scanner_range < 1:
        return False
    return (turn % ((scanner_range - 1) * 2)) == 0


def solve_puzzle_part_1(firewall: [int]) -> int:
    severity = 0
    for step, scanner_range in enumerate(firewall):
        if has_been_caught(step, scanner_range):
            severity += (step * scanner_range)
    return severity


def solve_puzzle_part_2(firewall: [int]) -> int:
    wait = 0

    while True:
        for step, depth in enumerate(firewall):
            if has_been_caught(step + wait, depth):
                wait += 1
                break
        else:
            return wait


if __name__ == "__main__":
    puzzle_input = get_input()

    solution_1 = solve_puzzle_part_1(puzzle_input)
    print(f'Part 1: {solution_1}')

    solution_2 = solve_puzzle_part_2(puzzle_input)
    print(f'Part 2: {solution_2}')

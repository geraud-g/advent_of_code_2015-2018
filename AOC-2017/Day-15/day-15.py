def get_input() -> [str]:
    with open('input.txt') as f:
        line = f.readline()
        return [int(x) for x in line.split(', ')]


def solve_puzzle(generator_a: int, generator_b: int) -> int:
    a_factor = 16807
    b_factor = 48271
    mod = 2147483647
    counter = 0
    mask = 65535
    for _ in range(40000000):
        generator_a = (generator_a * a_factor) % mod
        generator_b = (generator_b * b_factor) % mod
        if generator_a & mask == generator_b & mask:
            counter += 1
    return counter


def get_a_value(generator_a):
    a_factor = 16807
    mod = 2147483647
    while True:
        generator_a = (generator_a * a_factor) % mod
        if generator_a % 4 == 0:
            yield generator_a


def get_b_value(generator_b):
    b_factor = 48271
    mod = 2147483647

    while True:
        generator_b = (generator_b * b_factor) % mod
        if generator_b % 8 == 0:
            yield generator_b


def solve_puzzle2(generator_a: int, generator_b: int) -> int:
    mask = 65535
    counter = 0
    a_gen = get_a_value(generator_a)
    b_gen = get_b_value(generator_b)
    for x in range(5000000):
        a = next(a_gen)
        b = next(b_gen)
        if a & mask == b & mask:
            counter += 1

    return counter


if __name__ == "__main__":
    a = 783
    b = 325
    # puzzle_input = get_input()

    solution_1 = solve_puzzle(a, b)
    print(f'Part 1: {solution_1}')

    solution_2 = solve_puzzle2(a, b)
    print(f'Part 2: {solution_2}')

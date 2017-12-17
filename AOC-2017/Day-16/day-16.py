def spin(programs: [str], length: int) -> [str]:
    length = length % 16
    return programs[-length:] + programs[:-length]


def exchange(programs: [str], index_a: int, index_b: int) -> [str]:
    programs[index_a], programs[index_b] = programs[index_b], programs[index_a]
    return programs


def partner(programs: [str], name_a: str, name_b: str) -> [str]:
    index_a = programs.index(name_a)
    index_b = programs.index(name_b)
    programs[index_a], programs[index_b] = programs[index_b], programs[index_a]
    return programs


def get_input() -> [str]:
    moves = []

    with open('input.txt') as f:
        line = f.readline()
    for instruction in line.split(','):
        if instruction[0] == 's':
            action = spin
            *args, = [int(instruction[1:])]
        elif instruction[0] == 'x':
            action = exchange
            *args, = map(int, instruction[1:].split('/'))
        elif instruction[0] == 'p':
            action = partner
            *args, = instruction[1:].split('/')
        else:
            raise ValueError
        moves.append((action, tuple(args)))
    return tuple(moves)


def solve_puzzle(programs: [str], moves: [str]) -> [str]:
    for action, args in moves:
        programs = action(programs, *args)
    return programs


def solve_part_2(programs: [str], moves: [str]) -> [str]:
    history = []
    history_len = 0
    i = 0

    while i < 1000000000 - 1:
        if programs in history and (1000000000 - i) > history_len:
            programs = history[-1]
            i += (history_len - 1)
        else:
            history += [programs[:]]
            history_len += 1
            programs = solve_puzzle(programs, moves)
            i += 1

    return programs


if __name__ == "__main__":
    puzzle_input = get_input()
    progs = list(map(chr, range(ord('a'), ord('q'))))

    solution_1 = solve_puzzle(progs[:], puzzle_input)
    formatted_solution_1 = ''.join(solution_1)
    print(f'Part 1: {formatted_solution_1}')

    solution_2 = solve_part_2(progs[:], puzzle_input)
    formatted_solution_2 = ''.join(solution_2)
    print(f'Part 2: {formatted_solution_2}')

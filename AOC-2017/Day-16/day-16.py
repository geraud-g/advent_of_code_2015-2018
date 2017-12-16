import re


def get_input() -> [str]:
    with open('input.txt') as f:
        line = f.readline()
    return line.split(',')


def spin(programs, length):
    length = int(length) % len(programs)
    return programs[-length:] + programs[:-length]


def exchange(programs, index_a, index_b):
    programs[index_a], programs[index_b] = programs[index_b], programs[index_a]


def partner(programs, name_a, name_b):
    index_a = programs.index(name_a)
    index_b = programs.index(name_b)
    programs[index_a], programs[index_b] = programs[index_b], programs[index_a]


def solve_puzzle(programs: [str], moves: [str]) -> [str]:
    for move in moves:
        if move[0] == 's':
            programs = spin(programs, move[1:])
        elif move[0] == 'x':
            exchange(programs, *map(int,move[1:].split('/')))
        elif move[0] == 'p':
            partner(programs, *move[1:].split('/'))

    return programs


def solve_part_2(moves):
    programs = list(map(chr, range(ord('a'), ord('q'))))
    history = []
    i = 0

    while i < 1000000000 - 1:
        history_len = len(history)
        if programs in history and (1000000000 - i) > history_len:
            programs = history[-1]
            i += (history_len - 1)
        else:
            history += [programs[:]]
            programs = solve_puzzle(programs, moves)
            i += 1

    return programs


if __name__ == "__main__":
    puzzle_input = get_input()
    progs = list(map(chr, range(ord('a'), ord('q'))))

    solution_1 = solve_puzzle(progs, puzzle_input[:])
    formatted_solution_1 = ''.join(solution_1)
    print(f'Part 1: {formatted_solution_1}')

    solution_2 = solve_part_2(puzzle_input)
    formatted_solution_2 = ''.join(solution_2)
    print(f'Part 2: {formatted_solution_2}')
    print('fjpmholcibdgeakn')

from collections import defaultdict


def get_input() -> []:
    programs = {}
    with open('input.txt') as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        program_id, group = line.split(' <-> ')
        programs[program_id] = group.split(', ')
    return programs


def is_reachable(programs, start, end):

    visited = defaultdict(bool)

    queue = [start]
    visited[start] = True

    while queue:

        next = queue.pop(0)
        if next == end:
            return True

        for i in programs[next]:  # graph =
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return False


def solve_puzzle(programs: {}):
    count = 0

    for program, group in programs.items():
        if is_reachable(programs, program, '0'):
            count += 1

    return count


if __name__ == "__main__":
    puzzle_input = get_input()
    solution_1 = solve_puzzle(puzzle_input)

    print(f'Part 1: {solution_1}')
    # print(f'Part 2: {solution_2}')

from collections import defaultdict


def get_input() -> []:
    programs = {}
    with open('input.txt') as f:
        lines = f.readlines()
    for line in lines:
        program_id, group = line.strip().split(' <-> ')
        programs[program_id] = group.split(', ')
    return programs


def bfs(programs: {}, start: str, goal) -> (bool, defaultdict):
    visited = defaultdict(bool)
    queue = [start]
    visited[start] = True

    while queue:
        program_id = queue.pop(0)
        if program_id == goal:
            return True, visited

        for i in programs[program_id]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return False, visited


def solve_puzzle_part_1(programs: {}) -> int:
    count = 0
    for program, group in programs.items():
        reachable, _ = bfs(programs, program, '0')
        if reachable:
            count += 1
    return count


def solve_puzzle_part_2(programs: {}) -> int:
    groups = []
    for program in programs:
        _, group = bfs(programs, program, None)
        if group not in groups:
            groups.append(group)
    return len(groups)


if __name__ == "__main__":
    puzzle_input = get_input()

    solution_1 = solve_puzzle_part_1(puzzle_input)
    print(f'Part 1: {solution_1}')

    solution_2 = solve_puzzle_part_2(puzzle_input)
    print(f'Part 2: {solution_2}')

def cpy(registers, value, register):
    if value in registers:
        registers[register] = registers[value]
    else:
        registers[register] = int(value)


def inc(registers, value):
    registers[value] += 1


def dec(registers, value):
    registers[value] -= 1


def jnz(registers, to_compare, jump_to):
    value = registers[to_compare] if to_compare in registers else int(to_compare)
    if value != 0:
        return int(jump_to)


def proceed(instructions, puzzle_2=False):
    instruction_index = 0
    instructions_nbr = len(instructions)
    registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    if puzzle_2:
        registers['c'] = 1
    actions = {
        'cpy': cpy,
        'inc': inc,
        'dec': dec,
        'jnz': jnz
    }

    while instruction_index < instructions_nbr:
        instructions_nbr = max(0, instructions_nbr)
        instruction, *args = instructions[instruction_index]
        ret = actions[instruction](registers, *args)
        instruction_index += ret if ret else 1
    return registers


def parse_file():
    instructions = {}

    with open("input.txt") as f:
        instructions = {index: line.split() for (index, line) in enumerate(f.readlines())}
    return instructions


if __name__ == "__main__":
    instructions = parse_file()
    registers = proceed(instructions)
    print("Puzzle 1: the value of register a is {}".format(registers['a']))
    registers = proceed(instructions, puzzle_2=True)
    print("Puzzle 2: the value of register a is {}".format(registers['a']))
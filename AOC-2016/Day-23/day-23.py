def cpy(registers, instructions, instruction_index, value, register):
    if value in registers:
        registers[register] = registers[value]
    else:
        registers[register] = int(value)


def inc(registers, instructions, instruction_index, value):
    registers[value] += 1


def mult(registers, instructions, instruction_index, value):
    registers[value] += 1


def dec(registers, instructions, instruction_index, value):
    registers[value] -= 1


def jnz(registers, instructions, instruction_index, to_compare, jump_to):
    value = registers[to_compare] if to_compare in registers else int(to_compare)
    jump_to = registers[jump_to] if jump_to in registers else int(jump_to)
    if value != 0:
        return jump_to


def toggle(registers, instructions, instruction_index, value):
    value = registers[value] if value in registers else int(value)
    try:
        changed_instruction, *args = instructions[instruction_index + value]
    except KeyError:
        return
    if len(args) == 1:
        changed_instruction = "dec" if changed_instruction == "inc" else "inc"
    else:
        changed_instruction = "cpy" if changed_instruction == "jnz" else "jnz"
    instructions[instruction_index + value] = [changed_instruction] + args


def proceed(instructions, puzzle_2=False):
    instruction_index = 0
    instructions_nbr = len(instructions)
    registers = {'a': 7, 'b': 0, 'c': 0, 'd': 0}
    actions = {
        'tgl': toggle,
        'cpy': cpy,
        'inc': inc,
        'dec': dec,
        'jnz': jnz
    }
    if puzzle_2:
        registers['a'] = 12
        actions["inc"] = mult

    while instruction_index < instructions_nbr:
        instructions_nbr = max(0, instructions_nbr)
        instruction, *args = instructions[instruction_index]
        ret = actions[instruction](registers, instructions, instruction_index, *args)
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
    instructions = parse_file()
    registers = proceed(instructions, puzzle_2=True)
    print("Puzzle 2: the value of register a is {}".format(registers['a']))

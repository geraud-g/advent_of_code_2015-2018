import re

__author__ = 'Géraud'


def restrain_to_16_bytes(n):
    return n + 2**16 if n < 0 else n


def assign_value(circuits, instruction):
    if instruction[0].isdigit():
        circuits[instruction[2]] = int(instruction[0])
        return True
    elif instruction[0] in circuits:
        circuits[instruction[2]] = circuits[instruction[0]]
        return True
    return False


def complement(circuits, instruction):
    a = instruction[1]
    c = instruction[3]
    if a in circuits:
        a = circuits[a]
    elif a.isdigit():
        a = int(a)
    else:
        return False
    val = restrain_to_16_bytes(~ a)
    circuits[c] = val
    return True


def execute(circuits, instruction, operator):
    a = instruction[0]
    b = instruction[2]
    c = instruction[4]

    dic_operator = {
        "AND": lambda a1, b1: a1 & b1,
        "OR": lambda a1, b1: a1 | b1,
        "LSHIFT": lambda a1, b1: a1 << b1,
        "RSHIFT": lambda a1, b1: a >> b
    }
    if (a not in circuits and not a.isdigit()) or (b not in circuits and not b.isdigit()):
        return False
    a = circuits[a] if a in circuits else int(a)
    b = circuits[b] if b in circuits else int(b)
    val = restrain_to_16_bytes(dic_operator[operator](a, b))
    circuits[c] = val
    return True


def run_circuit(instructions, circuits):
    # We continue until all instructions are processed
    while not all(True if not value else False for value in instructions):

        for index, instruction in enumerate(instructions):
            operator = None

            # We already process this line
            if not instruction:
                continue
            # Variable assignation
            if len(instruction) == 3 and assign_value(circuits, instruction):
                instructions[index] = None
            # Instruction
            elif "NOT" in instruction:
                if complement(circuits, instruction):
                    instructions[index] = None
            elif "AND" in instruction:
                operator = "AND"
            elif "OR" in instruction:
                operator = "OR"
            elif "LSHIFT" in instruction:
                operator = "LSHIFT"
            elif "RSHIFT" in instruction:
                operator = "RSHIFT"

            if operator and execute(circuits, instruction, operator):
                instructions[index] = None

if __name__ == '__main__':
    circuits_a = dict()
    circuits_b = dict()

    with open('input.txt', 'r') as file:
        instructions = file.readlines()
        instructions_b = instructions[:]

    # Formatting instructions for part 1
    for index, instruction in enumerate(instructions):
        instructions[index] = instruction.split()
    # Solving part 1
    run_circuit(instructions, circuits_a)
    print("Part 1: %d" % circuits_a['a'])

    # Override value for 'b' assignment with the value 'a' found in part 1
    b_assignment_index = [n for n, x in enumerate(instructions_b) if re.match(r'^.+ -> b$', x)][0]
    instructions_b[b_assignment_index] = str(circuits_a['a']) + ' -> b'
    # Formatting instructions for part 2
    for index, instruction in enumerate(instructions_b):
            instructions_b[index] = instruction.split()
    # Solving part 2
    run_circuit(instructions_b, circuits_b)
    print("Part 2: %d" % circuits_b['a'])

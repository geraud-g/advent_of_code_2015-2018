import re
from collections import defaultdict


def get_input() -> []:
    instructions = []
    pattern = r'(\w+) (inc|dec) (-?\d+) if (\w+) ([<>=!]+) (-?\d+)'

    with open('input.txt') as f:
        for line in f.readlines():
            result = re.findall(pattern, line.strip())
            if result:
                instructions.append(result[0])
    return instructions


def compare(a: int, b: int, operator: str) -> bool:
    return {
        '==': lambda x, y: x == y,
        '!=': lambda x, y: x != y,
        '>=': lambda x, y: x >= y,
        '<=': lambda x, y: x <= y,
        '>': lambda x, y: x > y,
        '<': lambda x, y: x < y,
    }.get(operator)(a, b)


def iter_on_instructions(instructions: []) -> (int, int):
    registers = defaultdict(int)
    max_value_in_loop = 0

    for instruction in instructions:
        registry, operator, op_value, registry_to_compare, comparator, value_to_compare = instruction
        op_value = int(op_value)
        value_to_compare = int(value_to_compare)

        if compare(registers[registry_to_compare], value_to_compare, comparator):
            if operator == 'dec':
                op_value *= -1
            registers[registry] += op_value
            max_value_in_loop = max(max_value_in_loop, registers[registry])

    registers_values = [value for key, value in registers.items()]
    max_value_in_registers = max(registers_values)

    return max_value_in_registers, max_value_in_loop


if __name__ == "__main__":
    puzzle_input = get_input()
    part_1, part_2 = iter_on_instructions(puzzle_input)
    print(f"Puzzle 2: {part_1}")
    print(f"Puzzle 2: {part_2}")
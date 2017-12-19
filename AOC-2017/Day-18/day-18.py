def get_input() -> [[str]]:
    instructions = []

    with open('input.txt') as f:
        for line in f.readlines():
            args = []
            for value in line.split():
                try:
                    args += [int(value)]
                except ValueError:
                    args += [value]
            instructions.append(args)
    return instructions


class Program:
    def __init__(self, instructions, program_id: int, part: int=1):
        self.index = 0
        self.send_counter = 0
        self.instructions = instructions
        self.program_id = program_id
        self.part = part
        self.registers = {'p': program_id}
        self.own_queue = None
        self.other_queue = None

    def get(self, value) -> int:
        if isinstance(value, int):
            return value
        else:
            return self.registers[value]

    def snd(self, value):
        self.other_queue.append(self.get(value))
        self.send_counter += 1

    def rcv(self, value_a):
        if self.part == 1 and self.get(value_a) > 0:
            raise StopIteration
        elif not self.own_queue:
            self.index -= 1
        else:
            self.registers[value_a] = self.own_queue.pop(0)

    def set(self, value_a, value_b):
        new_value = self.get(value_b)
        self.registers[value_a] = new_value

    def add(self, value_a, value_b):
        new_value = self.get(value_b)
        self.registers[value_a] += new_value

    def mul(self, value_a, value_b):
        new_value = self.get(value_b)
        self.registers[value_a] *= new_value

    def mod(self, value_a, value_b):
        new_value = self.get(value_b)
        self.registers[value_a] %= new_value

    def jgz(self, value_a, value_b):
        value_to_compare = self.get(value_a)
        if value_to_compare > 0:
            self.index += (self.get(value_b) - 1)

    def execute_next_instruction(self):
        instruction = self.instructions[self.index]
        actions = {
            'get': self.get,
            'snd': self.snd,
            'set': self.set,
            'add': self.add,
            'mul': self.mul,
            'mod': self.mod,
            'rcv': self.rcv,
            'jgz': self.jgz,
        }
        next_instruction = actions[instruction[0]]
        self.index += 1
        return next_instruction(*instruction[1:])


def solve_puzzle(instructions: [[str]]) -> int:
    other_queue = []
    program = Program(instructions, program_id=0, part=1)
    program.other_queue = other_queue
    while True:
        try:
            program.execute_next_instruction()
        except StopIteration:
            break
    return program.other_queue[-1]


def solve_puzzle_part_2(instructions: [[str]]) -> int:
    program_a = Program(instructions, program_id=0, part=2)
    program_b = Program(instructions, program_id=1, part=2)
    queue_a = []
    queue_b = []
    program_a.own_queue, program_a.other_queue = queue_a, queue_b
    program_b.own_queue, program_b.other_queue = queue_b, queue_a
    a_last_index = None
    b_last_index = None

    while a_last_index != program_a.index or b_last_index != program_b.index:
        a_last_index = program_a.index
        b_last_index = program_b.index
        program_a.execute_next_instruction()
        program_b.execute_next_instruction()

    return program_b.send_counter


if __name__ == "__main__":
    puzzle_input = get_input()

    solution_1 = solve_puzzle(puzzle_input)
    print(f'Part 1: {solution_1}')

    solution_2 = solve_puzzle_part_2(puzzle_input)
    print(f'Part 2: {solution_2}')

__author__ = 'Géraud'


class Program:
    def __init__(self, instructions):
        self.instructions = instructions
        self.registers = {"a": 0, "b": 0}
        self.commands = {
            "hlf": self.half,
            "tpl": self.triple,
            "inc": self.increment,
            "jmp": self.jump,
            "jie": self.jump_even,
            "jio": self.jump_one
        }

    def half(self, args):
        self.registers[args[0]] //= 2
        return 1

    def triple(self, args):
        self.registers[args[0]] *= 3
        return 1

    def increment(self, args):
        self.registers[args[0]] += 1
        return 1

    @staticmethod
    def jump(args):
        return int(args[0])

    def jump_even(self, args):
        register = args[0].split(",")[0]
        distance = int(args[1])
        return distance if self.registers[register] % 2 == 0 else 1

    def jump_one(self, args):
        register = args[0].split(",")[0]
        distance = int(args[1])
        return distance if self.registers[register] == 1 else 1

    def execute(self, index, instruction):
        args = instruction.split()
        index += self.commands[args[0]](args[1:])
        return index

    def run(self):
        index = 0
        while True:
            try:
                index = self.execute(index, self.instructions[index])
            except IndexError:
                return self.registers

if __name__ == "__main__":
    program = []
    with open("input.txt", "r") as file:
        for line in file:
            program.append(line)

    pro = Program(program)
    values = pro.run()
    print("Part 1: {}".format(values['b']))

    pro = Program(program)
    pro.registers["a"] = 1
    values = pro.run()
    print("Part 2: {}".format(values['b']))

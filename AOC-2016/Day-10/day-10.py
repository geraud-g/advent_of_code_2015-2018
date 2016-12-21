from collections import defaultdict
import re


def parse_file():
    bots = defaultdict(list)
    instructions = []

    with open("input.txt") as f:
        for line in f.readlines():
            found = re.search(r'value ([\d ]+) goes to ([\w ]+)', line)
            if found:
                value = int(found.group(1))
                bot_id = found.group(2)
                bots[bot_id].append(value)
            else:
                instructions.append(line)
    return bots, instructions


def proceed(bots, instructions):
    bot = None

    while not all(x is None for x in instructions):
        for i, instruction in enumerate(instructions):
            if instruction is None:
                continue
            found = re.search(r'([\w ]+) gives low to ([\w ]+) and high to ([\w ]+)', instruction)
            if found:
                giver = found.group(1)
                receive_low = found.group(2)
                receive_high = found.group(3)

                if 61 in bots[giver] and 17 in bots[giver]:
                    bot = giver

                if len(bots[giver]) < 2:
                    continue

                bots[giver].sort()

                bots[receive_high].append(bots[giver].pop())
                bots[receive_low].append(bots[giver].pop(0))
                instructions[i] = None
    return bot


if __name__ == "__main__":
    bots, instructions = parse_file()
    bot = proceed(bots, instructions)

    print("Puzzle 1: {}".format(bot))

    value = bots['output 0'][0] * bots['output 1'][0] * bots['output 2'][0]
    print("Puzzle 2: {}".format(value))

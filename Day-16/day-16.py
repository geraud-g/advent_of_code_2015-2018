import re
import copy

__author__ = 'Géraud'


def count_matching_values(tape, sue, puzzle=1):
    count = 0
    for key in sue:
        # part 2
        if puzzle == 2 and (key == "cats" or key == "trees"):
            if sue[key] > tape[key]:
                count += 1
        elif puzzle == 2 and (key == "pomeranians" or key == "goldfish"):
            if sue[key] < tape[key]:
                count += 1
        elif sue[key] == tape[key]:
            count += 1
    sue["count"] = count


def parse_input(file):
    sues = dict()
    for line in file:
        regex = r'(\w+)[:, ]+(\d+)[:, ]*'
        match = re.findall(regex, line)
        if match:
            num = int(match[0][1])
            sues[num] = dict()
            for found in match[1:]:
                sues[num][found[0]] = int(found[1])
    return sues


if __name__ == "__main__":
    with open('input.txt') as file:
        sues = parse_input(file.readlines())
    tape = {"children": 3,
            "cats": 7,
            "samoyeds": 2,
            "pomeranians": 3,
            "akitas": 0,
            "vizslas": 0,
            "goldfish": 5,
            "trees": 3,
            "cars": 2,
            "perfumes": 1}
    sues_2 = copy.deepcopy(sues)
    # Part 1
    for key in sues:
        count_matching_values(tape, sues[key], puzzle=1)
    max_match = max([sues[sue]["count"] for sue in sues])
    for key in sues:
        if sues[key]["count"] == max_match:
            print("Part 1: {}".format(key))
            break
    # Part 2
    for key in sues_2:
        count_matching_values(tape, sues_2[key], puzzle=2)
    max_match = max([sues[sue]["count"] for sue in sues_2])
    for key in sues_2:
        if sues_2[key]["count"] == max_match:
            print("Part 2: {}".format(key))
            break

import itertools

__author__ = 'Géraud'


def parse_file(file):
    relations = dict()

    for line in file:
        split = line[:-2].split()
        person_a, person_b = split[0], split[10]
        happiness = int(split[3])
        if split[2] == "lose":
            happiness *= -1
        if person_a not in relations:
            relations[person_a] = {person_b: happiness}
        else:
            relations[person_a][person_b] = happiness
    return relations


def add_myself(relations):
    relations["myself"] = dict()
    for key in relations:
        if key != "myself":
            relations[key]["myself"] = 0
            relations["myself"][key] = 0


def calculate_max_change_in_happiness(relations):
    all_dispositions = itertools.permutations(relations.keys())
    happiness_change = []
    for disposition in all_dispositions:
        person_a = None
        count = 0
        for person_b in disposition:
            if person_a is None:
                first = person_b
                person_a = person_b
                continue
            count += relations[person_a][person_b]
            count += relations[person_b][person_a]
            person_a = person_b
        count += relations[first][person_b]
        count += relations[person_b][first]
        happiness_change.append(count)
    return max(happiness_change)


if __name__ == "__main__":
    part_puzzle = 2
    with open('input.txt') as file:
        file = file.readlines()

    relations = parse_file(file)
    max_happiness = calculate_max_change_in_happiness(relations)
    print("Part 1: {}".format(max_happiness))

    add_myself(relations)
    max_happiness = calculate_max_change_in_happiness(relations)
    print("Part 2: {}".format(max_happiness))

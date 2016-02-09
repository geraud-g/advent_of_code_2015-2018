__author__ = 'Géraud'


def parse_input(file):
    replacements = {}
    molecule = None

    for line in file:
        splitted = line[:-1].split(" => ")
        if len(splitted) == 2:
            key = splitted[0]
            replace = splitted[1]
            if key in replacements:
                replacements[key].append(replace)
            else:
                replacements[key] = [replace]
        elif splitted[0] != "":
            molecule = splitted[0]
    return replacements, molecule


if __name__ == '__main__':
    with open('input.txt') as file:
        replacements, medicine_molecule = parse_input(file)

    combinations = []
    skip = 0
    for index, molecule in enumerate(medicine_molecule):
        if skip > 0:
            skip -= 1
            continue
        if medicine_molecule[index:index + 2] in replacements:
            skip = 1
            replaces = replacements[medicine_molecule[index:index + 2]]
            slice_left = slice(0, index)
            slice_right = slice(index + 2, None)
        elif medicine_molecule[index] in replacements:
            replaces = replacements[medicine_molecule[index]]
            slice_left = slice(0, index)
            slice_right = slice(index + 1, None)
        else:
            replaces = []
        for replace in replaces:
            combinations.append(medicine_molecule[slice_left] + replace + medicine_molecule[slice_right])
    print("Part 1: {}".format(len(set(combinations))))

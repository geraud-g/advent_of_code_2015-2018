import itertools
import operator
import functools


def get_group(packages, weight_per_group):
    groups = []
    for comb_len in range(1, len(packages)):
        if len(groups) > 0:
            groups.sort()
            return groups[0]
        for group in itertools.combinations(packages, comb_len):
            if sum(group) == weight_per_group:
                group = list(group)
                group.sort()
                groups.append(group)
    return None


if __name__ == '__main__':
    with open('input.txt') as file:
        packages = list(map(int, [line[:-1] for line in file]))
        packages.sort()
        packages.reverse()
        weight_per_group_part1 = sum(packages) // 3
        weight_per_group_part2 = sum(packages) // 4

        result = get_group(packages, weight_per_group_part1)
        result = functools.reduce(operator.mul, result, 1)
        print("Part 1: {}".format(result))

        result = get_group(packages, weight_per_group_part2)
        result = functools.reduce(operator.mul, result, 1)
        print("Part 2: {}".format(result))

import itertools

__author__ = 'Géraud'


if __name__ == "__main__":
    with open("input.txt") as file:
        containers = tuple(map(int, file.readlines()))
    liters = 150

    combinations_nbr = 0
    combinations_nbr_index = None

    min_comb = 0
    containers_len = len(containers)
    all_combinations = itertools.combinations(containers, containers_len)

    for container_index in range(1, containers_len):
        all_combinations = itertools.combinations(containers, container_index)
        for combination in all_combinations:
            if sum(combination) == liters:
                if combinations_nbr_index is None:
                    combinations_nbr_index = container_index
                if combinations_nbr_index == container_index:
                    min_comb += 1
                combinations_nbr += 1

    print("Part 1: {}".format(combinations_nbr))
    print("Part 1: {}".format(min_comb))

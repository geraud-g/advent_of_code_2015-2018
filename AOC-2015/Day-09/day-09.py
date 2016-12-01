import itertools

__author__ = 'Géraud'


def parse_file(file):
    """
    Return a dict where: distances_dic[town_a][town_b] = distance_from_town_a_to_town_b
    """
    distances_dict = dict()
    for line in file:
        splitted_line = line.split()
        town_a, town_b = splitted_line[0], splitted_line[2]
        distance = int(splitted_line[4])
        if town_a not in distances_dict:
            distances_dict[town_a] = {town_b: distance}
        else:
            distances_dict[town_a][town_b] = distance
        if town_b not in distances_dict:
            distances_dict[town_b] = {town_a: distance}
        else:
            distances_dict[town_b][town_a] = distance
    return distances_dict


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        locations_list = file.readlines()

    distances_dict = parse_file(locations_list)
    all_routes = itertools.permutations(list(distances_dict.keys()))
    distances = []

    for route in all_routes:
        came_from = route[0]
        count = 0

        for town in route[1:]:
            count += distances_dict[came_from][town]
            came_from = town
        distances.append(count)

    print("Part 1: %d" % min(distances))
    print("Part 2: %d" % max(distances))

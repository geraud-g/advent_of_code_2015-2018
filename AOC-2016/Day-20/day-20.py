def parse_file():
    blacklist = []

    with open('input.txt') as f:
        for line in f.readlines():
            line = [int(c) for c in line.split('-')]
            blacklist.append(line)
    return blacklist


def get_lowest_allowed_ip(blacklist):
    min_allowed = 0
    inf = [float('inf'), float('inf')]

    while any(line != inf for line in blacklist):
        lower, upper = min(blacklist, key=lambda x: x[0])

        if lower > min_allowed + 1:
            return min_allowed + 1
        min_allowed = max(upper, lower, min_allowed)
        min_in_blacklist_index = blacklist.index([lower, upper])
        blacklist[min_in_blacklist_index] = inf
    return None


def get_nbr_allowed_ip(blacklist):
    blacklisted_ip_count = 0
    inf = [float('inf'), float('inf')]
    min_value = 0
    max_value = 0

    while any(line != inf for line in blacklist):
        lower, upper = min(blacklist, key=lambda x: x[0])

        if lower > max_value + 1:
            blacklisted_ip_count += (max_value - min_value + 1)
            min_value = lower

        max_value = max(max_value, upper)
        index = blacklist.index([lower, upper])
        blacklist[index] = inf

    blacklisted_ip_count += (max_value - min_value + 1)
    return 4294967295 - blacklisted_ip_count + 1


if __name__ == "__main__":
    blacklist = parse_file()
    ret = get_lowest_allowed_ip(blacklist)
    print("Puzzle 1: {}".format(ret))

    blacklist = parse_file()
    ret = get_nbr_allowed_ip(blacklist)
    print("Puzzle 2: {}".format(ret))

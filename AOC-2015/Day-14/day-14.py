import re

__author__ = 'Géraud'


def parse_input(f):
    reindeers = []
    for line in f:
        regex = r'\D+(\d+)\D+(\d+)\D+(\d+)'
        match = re.findall(regex, line)
        if match:
            match = [int(x) for x in match[0]]
            speed, speed_duration, rest_duration = match
            reindeers.append({"speed": speed,
                              "speed_duration": speed_duration,
                              "rest_duration": rest_duration,
                              "traveled": 0,
                              "points": 0})
    return reindeers


if __name__ == "__main__":
    part_puzzle = 1
    with open('input.txt') as file:
        reindeers_stats = parse_input(file.readlines())
    reindeers = [reindeer.copy() for reindeer in reindeers_stats]

    for sec in range(2503):
        for index, reindeer in enumerate(reindeers):
            if reindeer["speed_duration"] > 0:
                reindeer["traveled"] += reindeer["speed"]
                reindeer["speed_duration"] -= 1
            elif reindeer["rest_duration"] > 0:
                reindeer["rest_duration"] -= 1
                if reindeer["rest_duration"] == 0:
                    reindeer["speed_duration"] = reindeers_stats[index]["speed_duration"]
                    reindeer["rest_duration"] = reindeers_stats[index]["rest_duration"]
        distance_max = max([reindeer["traveled"] for reindeer in reindeers])
        for reindeer in reindeers:
            if reindeer["traveled"] == distance_max:
                reindeer["points"] += 1

    print("Part 1: {}".format(distance_max))
    print("Part 2: {}".format(max([reindeer["points"] for reindeer in reindeers])))

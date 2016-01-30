import json

__author__ = 'Géraud'


def walk_in_json(jobject, count, puzzle=1):
    if type(jobject) is list:
        for elem in jobject:
            count = walk_in_json(elem, count, puzzle)
    elif type(jobject) is dict:
        if puzzle == 2 and ("red" in jobject or "red" in jobject.values()):
            return count
        for key in jobject:
            count = walk_in_json(jobject[key], count, puzzle)
    elif type(jobject) is int:
        count += jobject
    return count

if __name__ == '__main__':
    with open("input.txt", "r") as file:
        json_object = json.loads(file.readline())
    # Part 1
    count = 0
    for j in json_object:
        count = walk_in_json(j, count, puzzle=1)
    print("puzzle 1: {}".format(count))
    # Part 2
    count = 0
    for j in json_object:
        count = walk_in_json(j, count, puzzle=2)
    print("puzzle 2: {}".format(count))

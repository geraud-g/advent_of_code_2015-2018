from itertools import groupby


__author__ = 'Géraud'


def increment_string(string):
    exploded = [x for x in string]

    for i in reversed(range(len(string))):
        if exploded[i] == 'z':
            exploded[i] = 'a'
        else:
            exploded[i] = chr(ord(exploded[i]) + 1)
            return ''.join(exploded)
    return ''.join(exploded)


def got_triple(string):
    for i in range(5):
        a_ord = ord(string[i])
        b_ord = ord(string[i + 1])
        c_ord = ord(string[i + 2])
        if a_ord + 1 == b_ord and b_ord + 1 == c_ord:
            return True
    return False


def got_two_doubles(string):
    splited = [tuple(group) for key, group in groupby(string)]
    count = sum((1 if len(group) >= 2 else 0 for group in splited))
    return count >= 2


def resolve_puzzle(string):
    while True:
        string = increment_string(string)
        if ('i' or 'o' or 'l') in string:
            continue
        if not got_triple(string):
            continue
        if not got_two_doubles(string):
            continue
        break
    return string

if __name__ == '__main__':
    string_1 = "cqjxjnds"

    solution = resolve_puzzle(string_1)
    print("puzzle 1: %s" % solution)

    string_2 = solution
    solution = resolve_puzzle(string_2)
    print("puzzle 2: %s" % solution)

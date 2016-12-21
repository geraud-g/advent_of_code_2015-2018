import re
import itertools


def swap(password, swap_type, x, y, puzzle_2=False):
    if puzzle_2:
            x, y = y, x

    if swap_type == "position":
        x = int(x)
        y = int(y)
        password[x], password[y] = password[y], password[x]
    elif swap_type == "letter":
        password = ["$" if c == x else c for c in password]
        password = [x if c == y else c for c in password]
        password = [y if c == "$" else c for c in password]
    return password


def rotate_based(password, letter, puzzle_2=False):
    if puzzle_2:
        for perm in itertools.permutations(password):
            index = perm.index(letter)
            steps = index + 1
            steps += (index >= 4)
            new_password = rotate(list(perm), "right", steps, puzzle_2=False)
            if password == new_password:
                return list(perm)

    index = password.index(letter)
    steps = index + 1
    steps += (index >= 4)
    return rotate(password, "right", steps)


def rotate(password, direction, steps, puzzle_2=False):
    steps = int(steps) % len(password)
    if direction == "right":
        steps = -steps

    if puzzle_2:
        steps = -steps

    password = password[steps:] + password[:steps]
    return password


def reverse(password, x, y, puzzle_2=False):
    x = int(x)
    y = int(y)
    password = password[:x] + password[x:y + 1][::-1] + password[y + 1:]
    return password


def move(password, x, y, puzzle_2=False):
    if puzzle_2:
        x, y = y, x
    x = int(x)
    y = int(y)
    tmp_val = password[x]
    del password[x]
    password.insert(y, tmp_val)
    return password


def solve(password, instructions, puzzle_2=False):
    actions = {
        "swap": swap,
        "rotate based": rotate_based,
        "rotate": rotate,
        "reverse": reverse,
        "move": move
    }
    kwargs = {"puzzle_2": puzzle_2}
    for i, (action, args) in enumerate(instructions):
        password = actions[action](password, *args, **kwargs)
    return password


def parse_input():
    actions = [r'(swap) (position) (\d+) with \w+ (\d+)',
               r'(swap) (letter) ([a-zA-Z+]) with \w+ ([a-zA-Z+])',
               r'(rotate based) on position of letter (\w+)',
               r'(rotate) (left|right) (\d+) step',
               r'(reverse) positions (\d+) \w+ (\d+)',
               r'(move) position (\d+) to position (\d+)']
    file = []
    with open('input.txt') as f:
        for line in f.readlines():
            for regex in actions:
                search = re.search(regex, line)
                if search:
                    action = search.groups()[0]
                    args = search.groups()[1:]
                    file.append((action, args))
                    break
    return file


if __name__ == "__main__":
    password = list('abcdefgh')
    instructions = parse_input()
    scrambled = solve(password, instructions)
    print("Puzzle 1: {}".format(''.join(scrambled)))

    to_unscramble = list("fbgdceah")
    unscrambled = solve(to_unscramble, instructions[::-1], puzzle_2=True)
    print("Puzzle 2: {}".format(''.join(unscrambled)))

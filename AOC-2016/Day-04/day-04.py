import collections
import re
import string

def rotate_x(s, nbr):
    alph = string.ascii_lowercase
    nbr %= 26
    rotated_alph = alph[nbr:] + alph[:nbr]
    rotate_char = lambda c: rotated_alph[alph.find(c)] if alph.find(c)>-1 else ' '
    return ''.join(map(rotate_char, s))

def get_most_used_letters(name):
    name = name.replace('-', '')
    count = collections.Counter(name)
    most_common = count.most_common(len(name))

    # sort by value, then by alphabetic order
    most_common = sorted(most_common, key=lambda x: (-x[1], x[0]))
    return [letter for letter, count in most_common[:5]]


def get_clean_input(file):
    clean_data = []
    found = re.findall(r'([a-z\-]+)(\d+)\[(\w+)\]', file)

    for name, room_id, checksum in found:
        room_id = int(room_id)
        most_used_letters = get_most_used_letters(name)
        clean_room = (most_used_letters, room_id, checksum)
        clean_data.append(clean_room)
    return clean_data


def get_sum_of_valid_id(data):
    count = 0
    for most_common, room_id, checksum in data:
        if all(c in most_common for c in checksum):
            count += room_id
    return count


if __name__ == "__main__":
    with open("input.txt") as f:
        file = f.read()
    clean_data = get_clean_input(file)
    sum_valid = get_sum_of_valid_id(clean_data)
    print("Puzzle 1: {}".format(sum_valid))

    with open("input.txt") as f:
        file = f.read()
    found = re.findall(r'([a-z\-]+)(\d+)\[\w+\]', file)
    for name, room_id in found:
        decrypted = rotate_x(name, int(room_id))
        if "north" in decrypted:
            print("Puzzle 2: {}-> {}".format(decrypted, room_id))


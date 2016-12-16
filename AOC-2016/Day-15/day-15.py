def fill_space(length, data):
    while len(data) < length:
        data += '0' + ''.join('1' if c == '0' else '0' for c in data[::-1])
    return data[:length]


def get_checksum(data):
    checksum = ''.join('1' if a == b else '0' for a, b in zip(data[::2], data[1::2]))
    if len(checksum) % 2 == 0:
        checksum = get_checksum(checksum)
    return checksum


if __name__ == "__main__":
    data = '10111100110001111'
    length_puzzle_1 = 272
    length_puzzle_2 = 35651584
    data = fill_space(length_puzzle_2, data)

    puzzle_1 = get_checksum(data[:length_puzzle_1])
    print("Puzzle 1: {}".format(puzzle_1))

    puzzle_2 = get_checksum(data)
    print("Puzzle 2: {}".format(puzzle_2))

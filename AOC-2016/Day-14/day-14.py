from hashlib import md5
from itertools import groupby


SALT = "qzyelonm{}"


def get_consecutive_letters(consecutive_dic, value, puzzle_part):
    if value not in consecutive_dic:
        hash_value = md5(value.encode()).hexdigest()
        if puzzle_part == 2:
            for _ in range(2016):
                hash_value = md5(hash_value.encode()).hexdigest()
        consecutive = [(k, len(list(g))) for k, g in groupby(hash_value)]
        consecutive_dic[value] = [(k, n) for k, n in consecutive if n > 2]
    return consecutive_dic[value]


def is_valid_key(consec_dic, index, letter, puzzle_part):
    for x in range(1 + index, 1001 + index):
        current_hash = SALT.format(x)
        consec = get_consecutive_letters(consec_dic, current_hash, puzzle_part)
        len_5 = [k for k, g in consec if g >= 5]
        if letter in len_5:
            return True
    return False


def solve_puzzle(puzzle_part):
    consec_dic = {}
    keys_found = 0
    index = -1

    while True:
        index += 1
        c_hash = SALT.format(index)
        current_try = get_consecutive_letters(consec_dic, c_hash, puzzle_part)
        if not current_try:
            continue
        if is_valid_key(consec_dic, index, current_try[0][0], puzzle_part):
            keys_found += 1
        if keys_found == 64:
            return(index)


if __name__ == "__main__":
    ret = solve_puzzle(1)
    print("Puzzle 1: {}".format(ret))

    ret = solve_puzzle(2)
    print("Puzzle 2: {}".format(ret))

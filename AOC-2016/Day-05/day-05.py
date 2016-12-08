from hashlib import md5
import itertools

def puzzle_1(value):
    str_encode = str.encode
    zeroes_str = "00000"
    letters_found_1 = 0
    letters_found_2 = 0
    code_1 = ""
    code_2 = ["", "", "", "", "", "", "", ""]

    for n in itertools.count():
        current_try = str_encode("%s%d" % (value, n))
        current_hash = md5(current_try).hexdigest()

        if current_hash.startswith(zeroes_str):
            if letters_found_1 < 8:
                code_1 += current_hash[5]
                letters_found_1 += 1

            if letters_found_2 < 8:
                index = current_hash[5]
                if index.isdigit():
                    index = int(index)
                    if index < 8 and code_2[index] == "":
                        code_2[index] = current_hash[6]
                        letters_found_2 += 1

            if letters_found_1 >= 8 and letters_found_2 >= 8:
                break

    code_2 = ''.join(code_2)
    return code_1, code_2

if __name__ == "__main__":
    value = "ffykfhsq"

    code_1, code_2 = puzzle_1(value)
    print("Puzzle 1: {}".format(code_1))
    print("Puzzle 2: {}".format(code_2))

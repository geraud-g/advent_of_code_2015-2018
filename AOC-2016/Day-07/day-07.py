import re


def got_abba(text):
    for i, c in enumerate(text[:-3]):
        if c == text[i+3] and text[i+1] == text[i+2] and text[i+1] != c:
            return True
    return False


def get_aba(text):
    aba_found = []
    for i, c in enumerate(text[:-2]):
        if c == text[i+2] and text[i+1] != c:
            aba_found.append(text[i: i + 3])
    return aba_found


def matching_aba_bab(supernet, hypernet):
    for sup in supernet:
        for aba in get_aba(sup):
            bab = "{}{}{}".format(aba[1], aba[0], aba[1])
            if any([bab in hyp for hyp in hypernet]):
                return True
    return False


def parse_file(file):
    parsed_file = []
    for line in file:
        hypernet = list(re.findall(r'\[([a-z]+)\]', line))
        leftover = re.sub(r'\[[a-z]+\]', " ", line)
        supernet = leftover.split()
        parsed_file.append((supernet, hypernet))
    return parsed_file


if __name__ == "__main__":
    counter_1 = 0
    counter_2 = 0
    with open("input.txt") as f:
        parsed_file = parse_file(f.readlines())

    # Puzzle 1
    
    for supernet, hypernet in parsed_file:
        if not any(map(got_abba, hypernet)) and any(map(got_abba, supernet)):
            counter_1 += 1
    print("Puzzle 1: {}".format(counter_1))

    # Puzzle 2
    for supernet, hypernet in parsed_file:
        counter_2 += matching_aba_bab(supernet, hypernet)
    print("Puzzle 2: {}".format(counter_2))

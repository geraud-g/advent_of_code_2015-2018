
def get_input() -> [[str]]:
    with open('input.txt') as f:
        return f.readlines()


def has_unique_passwords(line: str) -> bool:
    split_line = line.split()
    return len(split_line) == len(set(split_line))


def has_no_anagram(line: str) -> bool:
    sorted_split_line = [''.join(sorted(password)) for password in line.split()]
    return len(sorted_split_line) == len(set(sorted_split_line))


if __name__ == "__main__":
    pass_phrases = get_input()

    result_1 = sum(int(has_unique_passwords(pass_phrase)) for pass_phrase in pass_phrases)
    print(f"Puzzle 1: {result_1}")

    result_2 = sum(int(has_no_anagram(pass_phrase)) for pass_phrase in pass_phrases)
    print(f"Puzzle 2: {result_2}")


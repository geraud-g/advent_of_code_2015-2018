def puzzle(captcha: [int], part: int=1) -> int:
    captcha_len = len(captcha)
    sum_of_valid_digits = 0
    step = 1 if part == 1 else (captcha_len // 2)

    for index, value in enumerate(captcha):
        compare_index = (index + step) % captcha_len
        if value == captcha[compare_index]:
            sum_of_valid_digits += value

    return sum_of_valid_digits


if __name__ == "__main__":
    with open('input.txt') as f:
        captcha = list(map(int, f.read()))

    result_1 = puzzle(captcha, part=1)
    print(f"Puzzle 1: {result_1}")

    result_2 = puzzle(captcha, part=2)
    print(f"Puzzle 2: {result_2}")

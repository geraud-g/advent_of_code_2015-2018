def get_digit(keypad, start_position, instructions):
    digit = None
    movements = {
        "U": lambda y, x: (max(y-1, 0), x),
        "R": lambda y, x: (y, x+1),
        "D": lambda y, x: (y+1, x),
        "L": lambda y, x: (y, max(x-1, 0))
    }

    y, x = start_position
    for instruction in instructions:
        new_y, new_x = movements[instruction](y, x)
        try:
            new_digit = keypad[new_y][new_x]
            if new_digit is not None:
                y, x = new_y, new_x
                digit = new_digit
        except IndexError:
            pass
    return (y, x), digit

def get_code(instructions, keypad):
    bathroom_code = ""
    position = (1, 1)

    for instruct in instructions:
        position, digit = get_digit(keypad, position, instruct)
        bathroom_code += digit

    return bathroom_code

if __name__ == "__main__":
    keypad_puzzle_1 = (("1", "2", "3"), ("4", "5", "6"), ("7", "8", "9"))
    keypad_puzzle_2 = ((None, None, "1", None, None),
                        (None, "2", "3", "4", None),
                        ("5", "6", "7", "8", "9"),
                        (None, "A", "B", "C", None),
                        (None, None, "D", None, None))

    with open('input.txt') as f:
        file = f.read()
        file = file.split()
        code = get_code(file, keypad_puzzle_1)
        print("Puzzle 1: {}".format(code))
        code = get_code(file, keypad_puzzle_2)
        print("Puzzle 2: {}".format(code))
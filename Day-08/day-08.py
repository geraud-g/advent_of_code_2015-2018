__author__ = 'Géraud'


def count_chars(strings_list):
    literals_len = 0
    values_len = 0

    for line in strings_list:
        # literals_len is the number of characters of code in one string
        literals_len += len(line)
        # Number of loops to skip
        jump = 0

        for index, char in enumerate(line):
            line_len = len(line)
            # This char is part of a value already computed, so we skip it
            if jump > 0:
                jump -= 1
            # If the value is not an escaped quote:
            elif char != "\"":
                # Value is \\ or \", we skip the next char
                if char == "\\" and index + 1 < line_len and (line[index + 1] == "\\" or line[index + 1] == '"'):
                    jump = 1
                # Hexadecimal value, we skip the 3 next chars
                elif char == "\\" and index + 3 < line_len and (line[index + 1] == "x"):
                    jump = 3
                values_len += 1

    return literals_len, values_len


if __name__ == '__main__':
    circuits_a = dict()
    circuits_b = dict()

    with open('input.txt', 'r') as file:
        strings_list = file.readlines()
        literals_len, values_len = count_chars(strings_list)
        print("Part 1: %d" % (literals_len - values_len))

        strings_list = ["\\\"" + line.replace('\\', '\\\\').replace('\"', '\\\"') + "\\\"" for line in strings_list]
        literals_len, values_len = count_chars(strings_list)
        print("Part 2: %d" % (literals_len - values_len))


if __name__ == '__main__':
    targeted_row = 2978
    targeted_column = 3083
    multiply = 252533
    modulo = 33554393
    current_row = 1
    current_column = 1
    current_code = 20151125

    while current_column != targeted_column or current_row != targeted_row:
        current_code = (current_code * multiply) % modulo
        if current_row == 1:
            current_row = current_column + 1
            current_column = 1
        else:
            current_row -= 1
            current_column += 1

    print("Part {}: {}".format(1, current_code))

from itertools import count


def get_square_level_and_side_len(data: int) -> (int, int):
    for index, value in enumerate(count(start=1, step=2)):
        if value ** 2 > data:
            return index, value


def get_value_axis(data_location: int, side_len: int) -> int:
    start_value = (side_len - 2)**2 + 1
    end_value = side_len ** 2
    square = [end_value] + list(range(start_value, end_value + 1))
    position_on_side = square.index(data_location) % (side_len - 1)
    axis = abs(position_on_side - side_len // 2)
    return axis


def puzzle_1(data_location: int) -> int:
    square_level, square_side_len = get_square_level_and_side_len(data_location)
    alignment = get_value_axis(data_location, square_side_len)
    return square_level + alignment


def puzzle_2(data_locagion: int) -> int:
    return 2


if __name__ == "__main__":
    puzzle_input = 368078

    result_1 = puzzle_1(puzzle_input)
    print(f"Puzzle 1: {result_1}")


def get_evenly_divisible_values(row: [int]) -> (int, int):
    row = sorted(row, reverse=True)

    for index, value in enumerate(row):
        for sub_value in row[index + 1:]:
            if value % sub_value == 0:
                return value, sub_value
    raise ValueError("No evenly divisible values found.")


def get_checksum(spreadsheet: [[int]], part: int=1) -> int:
    checksum = 0

    for row in spreadsheet:
        if part == 1:
            checksum += max(row) - min(row)
        else:
            a, b = get_evenly_divisible_values(row)
            checksum += (a // b)
    return checksum


def get_input() -> [[int]]:
    spreadsheet = []
    with open('input.txt') as f:
        for line in f.readlines():
            line = [int(num) for num in line.split()]
            spreadsheet.append(line)
    return spreadsheet


if __name__ == "__main__":
    spreadsheet = get_input()

    result_1 = get_checksum(spreadsheet, part=1)
    print(f"Puzzle 1: {result_1}")

    result_2 = get_checksum(spreadsheet, part=2)
    print(f"Puzzle 2: {result_2}")


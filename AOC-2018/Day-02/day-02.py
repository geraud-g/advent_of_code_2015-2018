from collections import Counter
import itertools


def read_file() -> [str]:
    with open("input.txt") as f:
        return [x.strip() for x in f.readlines()]


def puzzle_part_b() -> str:
    boxes = read_file()
    line_len = len(boxes[0])
    box_hash = None

    for box_a, box_b in itertools.product(boxes, boxes):
        same_chars = [a for a, b in zip(box_a, box_b) if a == b]
        if len(same_chars) == line_len - 1:
            box_hash = "".join(same_chars)
            break
    return box_hash


def puzzle_part_a() -> int:
    boxes = read_file()
    doubles = 0
    triples = 0

    for box in boxes:
        has_double = False
        has_triple = False
        for _, count in Counter(box).items():
            if count == 2:
                has_double = True
            if count == 3:
                has_triple = True
        doubles += has_double
        triples += has_triple

    return doubles * triples


if __name__ == "__main__":
    result_a = puzzle_part_a()
    print(f"Puzzle part 1: {result_a}")
    result_b = puzzle_part_b()
    print(f"Puzzle part 2: {result_b}")

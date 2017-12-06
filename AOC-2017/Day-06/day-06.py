def get_input() -> [int]:
    with open('input.txt') as f:
        return [int(x) for x in f.readline().split()]


def redistributions(memory: [int], part: int=1) -> (int, [int]):
    computed = [memory]
    memory_len = len(memory)
    current_memory = memory[:]
    steps = 0

    while True:
        max_value = max(current_memory)
        max_value_index = current_memory.index(max_value)
        current_memory[max_value_index] = 0

        for index in range(max_value):
            tmp_index = (index + max_value_index + 1) % memory_len
            current_memory[tmp_index] += 1
        steps += 1
        if part == 1 and current_memory in computed:
            return steps, current_memory
        elif part == 2 and current_memory == memory:
            return steps
        else:
            computed.append(current_memory[:])


if __name__ == "__main__":
    puzzle_input = get_input()
    result_1, memory_final_state = redistributions(puzzle_input, part=1)
    print(f"Puzzle 1: {result_1}")

    result_2 = redistributions(memory_final_state, part=2)
    print(f"Puzzle 2: {result_2}")

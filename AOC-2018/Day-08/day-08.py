class Node:
    def __init__(self, metadata, children):
        self.metadata = metadata
        self.children = children

    def count_metadata(self):
        total = sum(self.metadata)
        for children in self.children:
            total += children.count_metadata()
        return total

    def count_metadata_part_b(self):
        total = 0

        if not self.children:
            return sum(self.metadata)

        for index in self.metadata:
            try:
                child = self.children[index - 1]
                total += child.count_metadata_part_b()
            except IndexError:
                pass
        return total


def read_file():
    with open("input.txt") as f:
        lines = f.readline()
    return [int(x) for x in lines.split()]


def populate_node(instructions):
    children_nbr, len_metadata = instructions[:2]
    instructions = instructions[2:]
    children_nodes = []

    for _ in range(children_nbr):
        node, instructions = populate_node(instructions)
        children_nodes.append(node)
    metadata = instructions[:len_metadata]
    instructions = instructions[len_metadata:]
    node = Node(metadata, children_nodes)
    return node, instructions


def puzzle_part_a() -> int:
    instructions = read_file()
    first_node, instructions = populate_node(instructions)
    return first_node.count_metadata()


def puzzle_part_b() -> int:
    instructions = read_file()
    first_node, instructions = populate_node(instructions)
    return first_node.count_metadata_part_b()


if __name__ == "__main__":
    result_a = puzzle_part_a()
    print(f"Puzzle part 1: {result_a}")
    result_b = puzzle_part_b()
    print(f"Puzzle part 2: {result_b}")

import re


class Node:
    def __init__(self, name: str, weight: int):
        self.name: str = name
        self.weight = weight
        self.children = {}


def get_input() -> {}:
    puzzle_input = {}
    pattern = r'(\w+) \((\d+)\)(?: -> (.+))?'

    with open('input.txt') as f:
        for line in f.readlines():
            result = re.findall(pattern, line)
            if result:
                name, weight, children = result[0]
                children = children.split(', ')
                if children == ['']:
                    children = []
                puzzle_input[name] = Node(name, int(weight))
                for x in children:
                    puzzle_input[name].children[x] = None
    return puzzle_input


def build_tree(tower: {}):
    for name, node in tower.items():
        for child in node.children:
            if node.children[child] is None:
                node.children[child] = tower[child]

    for name, node in tower.items():
        if all(name not in val.children for k, val in tower.items()):
            root = tower[name]
    return root


def get_tree_total_weight(tree):
    total = tree.weight
    for child in tree.children:
        total += get_tree_total_weight(tree.children[child])
    return total


if __name__ == "__main__":
    tower = get_input()
    tree = build_tree(tower)

    print(f"Puzzle 1: {tree.name}")


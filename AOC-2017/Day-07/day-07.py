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


def get_right_weight(tree: Node) -> (bool, int):
    total = tree.weight
    children_weight = []

    for child in tree.children:
        found, weight = get_right_weight(tree.children[child])
        if found:
            return True, weight
        children_weight.append(weight)

    if len(set(children_weight)) > 1:
        bad_weight_index, bad_weight = [(i, x) for i, x in enumerate(children_weight) if children_weight.count(x) == 1][0]
        good_weight = [x for x in children_weight if children_weight.count(x) > 1][0]
        bad_node_key = [x for x in tree.children][bad_weight_index]
        bad_node = tree.children[bad_node_key]
        print(f'Good weight: {good_weight}')
        print(f'Bad weight: {bad_weight}')
        print(f'Bad Node Weight and Name: {bad_node.weight}, {bad_node.name}')
        return True, ((good_weight - bad_weight) + bad_node.weight)

    return False, total + sum(children_weight)


if __name__ == "__main__":
    tower = get_input()
    tree = build_tree(tower)

    print(f"Puzzle 1: {tree.name}")

    _, puzzle_2 = get_right_weight(tree)
    print(f"Puzzle 2: {puzzle_2}")

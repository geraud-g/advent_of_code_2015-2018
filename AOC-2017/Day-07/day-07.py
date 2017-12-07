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
                puzzle_input[name] = (int(weight), children)
    return puzzle_input


def populate_children(tower: {}, node: Node, children: {}):
    for child_name in children:
        value = tower[child_name]

        if value is None:
            continue
        weight, child_children = value
        new_node = Node(child_name, weight)
        tower[child_name] = None

        populate_children(tower, new_node, child_children)
        node.children[child_name] = new_node


def build_tree(tower: {}):
    assigned = []
    for name, value in tower.items():
        if value is None:
            continue
        weight, children = value
        new_node = Node(name, weight)
        populate_children(tower, new_node, children)
        assigned.append(new_node)

    root_name = [name for name, node in tower.items() if node is not None][0]

    root = list(filter(lambda x: x.name == root_name, assigned))[0]
    return root


if __name__ == "__main__":
    tower = get_input()

    tree = build_tree(tower)
    print(f"Puzzle 1: {tree.name}")

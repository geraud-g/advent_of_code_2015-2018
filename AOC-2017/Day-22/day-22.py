from collections import defaultdict
from typing import Dict, Tuple

CLEAN = 0
INFECTED = 1
WEAKENED = 2
FLAGGED = 3

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


class Virus:
    directions_modifier = {
        CLEAN: -1,
        INFECTED: 1,
    }
    nodes_modifier = {
        INFECTED: CLEAN,
        CLEAN: INFECTED
    }
    nbr_burst = 10000

    def __init__(self, grid: Dict[Tuple, int], y: int, x: int):
        self.grid = grid
        self.y = y
        self.x = x
        self.direction = UP
        self.infected = 0

    def _rotate(self) -> None:
        node_value = self.grid[(self.y, self.x)]
        direction_modifier = self.directions_modifier[node_value]
        self.direction = (self.direction + direction_modifier) & 3

    def _update_node(self) -> None:
        coordinates = (self.y, self.x)
        new_node_value = self.nodes_modifier[self.grid[coordinates]]
        self.grid[coordinates] = new_node_value
        if new_node_value == INFECTED:
            self.infected += 1

    def _move(self) -> None:
        position_modifier = {
            UP: (-1, 0),
            RIGHT: (0, +1),
            DOWN: (1, 0),
            LEFT: (0, -1)
        }
        modifier_y, modifier_x = position_modifier[self.direction]
        self.y += modifier_y
        self.x += modifier_x

    def burst(self) -> None:
        for _ in range(self.nbr_burst):
            self._rotate()
            self._update_node()
            self._move()


class VirusB(Virus):
    directions_modifier = {
        CLEAN: -1,
        INFECTED: +1,
        WEAKENED: 0,
        FLAGGED: 2
    }
    nodes_modifier = {
        CLEAN: WEAKENED,
        WEAKENED: INFECTED,
        INFECTED: FLAGGED,
        FLAGGED: CLEAN
    }
    nbr_burst = 10000000


def get_virus(part: int) -> Virus:
    grid = defaultdict(int)
    virus_class = Virus if part == 1 else VirusB

    with open('input.txt') as f:
        grid_file = f.readlines()
    for y, row in enumerate(grid_file):
        for x, node in enumerate(row):
            if node == '#':
                grid[(y, x)] = INFECTED

    start_y = len(grid_file) // 2
    start_x = len(grid_file[0].strip()) // 2
    virus = virus_class(grid, start_y, start_x)
    return virus


if __name__ == '__main__':
    virus_a = get_virus(part=1)
    virus_a.burst()
    print(f'Puzzle part 1: {virus_a.infected}')

    virus_b = get_virus(part=2)
    virus_b.burst()
    print(f'Puzzle part 2: {virus_b.infected}')

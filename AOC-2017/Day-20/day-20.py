import math
import re
from collections import defaultdict

from typing import List


class Coordinates:
    def __init__(self, string):
        x, y, z = map(int, string.split(','))
        self.x: int = x
        self.y: int = y
        self.z: int = z

    def __str__(self):
        return f'<{self.x}, {self.y}, {self.z}>'


class Particle:
    def __init__(self, point_id, position, velocity, acceleration):
        self.id = point_id
        self.position: Coordinates = position
        self.velocity: Coordinates = velocity
        self.acceleration: Coordinates = acceleration

    def update(self) -> None:
        self.velocity.x += self.acceleration.x
        self.velocity.y += self.acceleration.y
        self.velocity.z += self.acceleration.z
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y
        self.position.z += self.velocity.z

    def distance_from_zero(self) -> float:
        x, y, z = self.position.x, self.position.y, self.position.z
        return math.sqrt(x**2 + y**2 + z**2)

    def __str__(self):
        return f'{self.id}: p={self.position}, v={self.velocity}, a={self.acceleration}'


def get_input() -> List[Particle]:
    points = []
    with open('input.txt') as f:
        for index, line in enumerate(f.readlines()):
            coord_x, coord_y, coord_z = map(Coordinates, re.findall(r'p=<(.+)>, v=<(.+)>, a=<(.+)>', line)[0])
            points += [Particle(index, coord_x, coord_y, coord_z)]
    return points


def remove_collisions(particles: List[Particle]) -> List[Particle]:
    coordinates_counter = defaultdict(int)
    for particle in particles:
        coordinates_counter[(particle.position.x, particle.position.y, particle.position.z)] += 1
    duplicates = [point for point in particles if coordinates_counter[(point.position.x, point.position.y, point.position.z)] > 1]
    for dup in duplicates:
        particles.remove(dup)
    return particles


def closest_to_zero(points: List[Particle]) -> Particle:
    for x in range(1000):
        for point in points:
            point.update()
    return min(points, key=lambda p: abs(p.distance_from_zero()))


def get_particles_left(particles: List[Particle]) -> List[Particle]:
    for x in range(1000):
        particles = remove_collisions(particles)
        for point in particles:
            point.update()
        particles = remove_collisions(particles)
    return particles


if __name__ == "__main__":
    puzzle_input = get_input()
    closest = closest_to_zero(puzzle_input)
    print(f'Puzzle part 1: {closest.id}')

    puzzle_input = get_input()
    particles_left = get_particles_left(puzzle_input)
    print(f'Puzzle part 2: {len(particles_left)}')

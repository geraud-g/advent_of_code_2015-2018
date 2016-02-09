from itertools import combinations, product

__author__ = 'Géraud'


def get_equipment():
    weapons = {
        "Dagger": {"cost": 8, "damage": 4, "armor": 0},
        "Shortsword": {"cost": 10, "damage": 5, "armor": 0},
        "Warhammer": {"cost": 25, "damage": 6, "armor": 0},
        "Longsword": {"cost": 40, "damage": 7, "armor": 0},
        "Greataxe": {"cost": 74, "damage": 8, "armor": 0}
    }
    armors = {
        "Leather": {"cost": 13, "damage": 0, "armor": 1},
        "Chainmail": {"cost": 31, "damage": 0, "armor": 2},
        "Splintmail": {"cost": 53, "damage": 0, "armor": 3},
        "Bandedmail": {"cost": 75, "damage": 0, "armor": 4},
        "Platemail": {"cost": 102, "damage": 0, "armor": 5},
        "None": {"cost": 0, "damage": 0, "armor": 0}
    }
    rings = {
        "Damage +1": {"cost": 25, "damage": 1, "armor": 0},
        "Damage +2": {"cost": 50, "damage": 2, "armor": 0},
        "Damage +3": {"cost": 100, "damage": 3, "armor": 0},
        "Defense +1": {"cost": 20, "damage": 0, "armor": 1},
        "Defense +2": {"cost": 40, "damage": 0, "armor": 2},
        "Defense +3": {"cost": 80, "damage": 0, "armor": 3},
        "None1": {"cost": 0, "damage": 0, "armor": 0},
        "None2": {"cost": 0, "damage": 0, "armor": 0}
    }
    weapons_index = [k for k in weapons]
    armors_index = [k for k in armors]
    rings_index = [k for k in rings]

    rings_comb = combinations(rings_index, 2)
    stuff_comb = product(weapons_index, armors_index)
    total_comb = product(stuff_comb, rings_comb)
    for stuff in total_comb:
        stuff = [stuff[0][0]] + [stuff[0][1]] + [stuff[1][0]] + [stuff[1][1]]
        ret = {
            "weapon": weapons[stuff[0]],
            "body_armor": armors[stuff[1]],
            "ring1": rings[stuff[2]],
            "ring2": rings[stuff[3]]
        }
        yield ret


class Player:
    def __init__(self, weapon, body_armor, ring1, ring2):
        self.weapon = weapon
        self.body_armor = body_armor
        self.ring1 = ring1
        self.ring2 = ring2
        self.hp = 100
        self.damage = weapon["damage"] + ring1["damage"] + ring2["damage"]
        self.armor = body_armor["armor"] + ring1["armor"] + ring2["armor"]
        self.cost = weapon["cost"] + body_armor["cost"] + ring1["cost"] + ring2["cost"]

    def won_fight(self):
        boss = {"hp": 103,
                "damage": 9,
                "armor": 2
                }
        while True:
            player_damage = self.damage - boss["armor"]
            player_damage = 1 if player_damage < 1 else player_damage
            boss_damage = boss["damage"] - self.armor
            boss_damage = 1 if boss_damage < 1 else boss_damage
            boss["hp"] -= player_damage
            if boss["hp"] < 1:
                return True, self.cost
            self.hp -= boss_damage
            if self.hp < 1:
                return False, self.cost


if __name__ == "__main__":
    won_min_cost = float("inf")
    lose_max_cost = -1

    for stuff in get_equipment():
        you = Player(**stuff)
        won, cost = you.won_fight()
        if won and cost < won_min_cost:
            won_min_cost = cost
        elif not won and cost > lose_max_cost:
            lose_max_cost = cost

    print("Part 1: {}".format(won_min_cost))
    print("Part 2: {}".format(lose_max_cost))
